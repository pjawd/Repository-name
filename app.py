import streamlit as st
import subprocess
import os

st.set_page_config(page_title="Twitter 媒体无广告下载", page_icon="📥", layout="centered")

st.title("📥 Twitter / X 无广告下载器")
st.caption("粘贴链接，一键下载无水印视频与高清图片")

url = st.text_input("请输入推特链接 (X/Twitter):", placeholder="https://x.com/...")

if st.button("开始解析下载", type="primary"):
    if not url:
        st.warning("请先输入有效的链接！")
    else:
        with st.spinner("正在努力解析中，请稍候..."):
            os.makedirs("downloads", exist_ok=True)
            
            cmd = [
                "yt-dlp",
                "-P", "downloads",
                "-o", "%(id)s.%(ext)s",
                url
            ]
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            downloaded_files = os.listdir("downloads")
            if downloaded_files:
                st.success("解析成功！点击下方按钮下载到设备：")
                for file in downloaded_files:
                    file_path = os.path.join("downloads", file)
                    with open(file_path, "rb") as f:
                        st.download_button(
                            label=f"💾 点击保存: {file}",
                            data=f,
                            file_name=file,
                            mime="application/octet-stream"
                        )
                # 清理临时文件
                for f in downloaded_files:
                    try:
                        os.remove(os.path.join("downloads", f))
                    except:
                        pass
            else:
                st.error("解析失败，请确保推文公开且链接正确。")
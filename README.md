# 🌟 奇妙星律动：儿童 AI 互动舞蹈乐园 (Kids AI Dance Star World)

专为 **4~6 岁学龄前幼儿** 与家庭/幼儿园大屏场景打造的 **儿童 AI 体感互动舞蹈教学系统**。

[![GitHub Pages](https://img.shields.io/badge/Deploy-GitHub%20Pages-brightgreen)](https://pages.github.com/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## ✨ 核心功能特色

1. **8 段专属循环舞蹈视频示范 (Loop Dance Videos)**：
   * 针对晨间律动曲《Morning Sunshine Hello》，每个动作独立生成 5 秒无缝循环舞蹈动画影片（小草摇摆、升小太阳、大挥手、抓阳光、小兔跳、比心送光波等），随时间轴自动无缝切源！
2. **多人体态骨架追踪 (1~3 人同屏互动)**：
   * 调取摄像头在画面中实时绘制发光骨骼关键点（肩、肘、腕、髋、膝、踝）。
   * 支持 **1人跟学、2人双人舞、3人派对** 模式，动作到位肢体瞬间爆星发光得分！
3. **亲切名师原声口令与伴奏音量避让 (Audio Ducking)**：
   * 告别生硬机械音，内置 12 段甜美温暖的幼教老师原声引导；口令响起时背景伴奏自动微降音量，凸显亲切人声。
4. **超大同步卡拉OK歌词**：
   * 极简界面设计，底部超大字号英汉双语歌词与节拍动态滚动。

---

## 🚀 如何发布并公开到 GitHub Pages（人人皆可在线访问）

本项目已完全做好静态化优化，所有媒体资源均采用相对路径，可**零成本一键部署到 GitHub Pages**：

### 步骤 1：在 GitHub 上创建一个新的公开仓库 (Public Repo)
1. 登录你的 [GitHub](https://github.com/) 账号；
2. 点击右上角 `+` -> **New repository**；
3. 输入仓库名（例如：`kai-music-ai-dance`），选择 **Public**，点击 **Create repository**。

### 步骤 2：推送本地代码到 GitHub
在终端中进入项目目录，执行以下命令（将 `<你的GitHub仓库URL>` 替换为实际地址）：

```bash
cd "/Volumes/4T M2 SSD/AI Native Company OS/Kai_Music"

# 初始化 Git 并提交代码
git init
git add .
git commit -m "feat: release kids AI dance star world v3.0"

# 关联远程仓库并推送
git branch -M main
git remote add origin <你的GitHub仓库URL>
git push -u origin main
```

*(或者直接运行项目根目录下的自动化脚本：`./deploy_to_github.sh <你的GitHub仓库URL>`)*

### 步骤 3：在 GitHub 仓库中开启 GitHub Pages
1. 打开你在 GitHub 上的该仓库页面；
2. 点击上方 **Settings**（设置）标签；
3. 在左侧菜单点击 **Pages**；
4. 在 **Build and deployment -> Source** 下拉菜单中：
   * Branch 选择 **`main`**
   * Folder 路径选择 **`/docs`**（或 `/ (root)`，如果使用 docs）
5. 点击 **Save**（保存）。
6. 等待 1~2 分钟，GitHub 就会生成你的公开专属访问网址：  
   👉 **`https://<你的GitHub用户名>.github.io/<仓库名>/`**

---

## 📂 项目目录结构

```
Kai_Music/
├── docs/                 # GitHub Pages 部署专属目录 (包含全套网页与媒体)
│   ├── index.html        # 主页面 (歌曲大厅 + 跳舞互动教室)
│   ├── videos/           # 8 支动作专属循环影片 (.mp4)
│   ├── voices/           # 12 段名师原声口令音频 (.mp3)
│   └── morning_sunshine_hello.mp3 # 背景音乐伴奏
├── web_app/              # 本地开发与调试目录
├── NOTION_DANCE_PROJECT.md # 项目全套规范与更新记录
├── deploy_to_github.sh   # 一键推送到 GitHub 辅助脚本
└── README.md
```

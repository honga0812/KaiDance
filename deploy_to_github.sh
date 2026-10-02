#!/bin/bash
# ==============================================================
# 奇妙星律动：一键部署到 GitHub Pages 自动化脚本
# 用法: ./deploy_to_github.sh <你的 GitHub 仓库远程地址>
# 例如: ./deploy_to_github.sh git@github.com:username/kai-music-ai-dance.git
# ==============================================================

set -e

REPO_URL=$1

if [ -z "$REPO_URL" ]; then
  echo "❌ 错误: 请传入你的 GitHub 仓库地址！"
  echo "👉 用法示例: ./deploy_to_github.sh https://github.com/your-username/kai-music-ai-dance.git"
  exit 1
fi

echo "🚀 开始准备部署到 GitHub..."

# 确保在项目根目录
cd "$(dirname "$0")"

# 同步最新的 web_app 到 docs/
echo "📦 同步最新静态文件至 docs/ ..."
mkdir -p docs
cp -r web_app/* docs/

# 初始化 git (若未初始化)
if [ ! -d ".git" ]; then
  echo "🔧 初始化本地 Git 仓库..."
  git init
  git branch -M main
fi

# 检查 remote
if git remote | grep -q 'origin'; then
  git remote set-url origin "$REPO_URL"
else
  git remote add origin "$REPO_URL"
fi

echo "📝 提交代码变更..."
git add .
git commit -m "feat: deploy kids AI dance star world to GitHub Pages" || true

echo "⬆️ 推送代码到 GitHub ($REPO_URL)..."
git push -u origin main

echo ""
echo "🎉 推送成功！"
echo "👉 请前往 GitHub 仓库页面："
echo "   Settings -> Pages -> Branch: main, Folder: /docs -> 点击 Save"
echo "   约 1 分钟后即可公开在线访问！"

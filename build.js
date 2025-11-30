const { execSync } = require('child_process');
const path = require('path');

console.log('🚀 Building GitHub Action...');

// 安装依赖
console.log('📦 Installing dependencies...');
try {
  execSync('npm install', { stdio: 'inherit' });
} catch (error) {
  console.error('❌ Failed to install dependencies:', error.message);
  process.exit(1);
}

// 使用ncc构建
console.log('🔨 Building with ncc...');
try {
  execSync('npx @vercel/ncc build src/index.js --license licenses.txt', { stdio: 'inherit' });
} catch (error) {
  console.error('❌ Failed to build with ncc:', error.message);
  process.exit(1);
}

console.log('✅ Build completed successfully!');
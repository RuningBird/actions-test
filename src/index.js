const core = require('@actions/core');
const { execSync } = require('child_process');

try {
  // 获取输入参数
  const message = core.getInput('message') || 'Hello from custom action!';
  
  // 执行主要逻辑
  console.log('Running custom action...');
  console.log(`Message: ${message}`);
  
  // 设置输出
  const result = `Processed: ${message}`;
  core.setOutput('result', result);
  
  // 打印结果
  console.log(`✅ Action completed successfully!`);
  console.log(`📝 Result: ${result}`);

} catch (error) {
  // 设置失败状态
  core.setFailed(`Action failed: ${error.message}`);
  console.error('❌ Error:', error.message);
}
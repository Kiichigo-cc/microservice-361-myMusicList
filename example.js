const child_process = require('child_process')

const exportpy = 'export.py';
const argument = 'pOg, database.js';

const runPython = child_process.execSync('python3 ${exportpy} ${argument.join(' ')}').toString();
console.log(runPython)
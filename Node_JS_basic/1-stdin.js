console.log('Welcome to Holberton School, what is your name?');
process.stdin.on('data', (data) => {
  const name = data.toString().trim();
  if (name !== '') {
    process.stdout.write(`Your name is: ${name}\n`);
  } else {
    process.exit();
  }
});

process.stdin.on('end', () => {
  console.log('This important software is now closing');
  process.exit();
});
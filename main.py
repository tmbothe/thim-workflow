import os
from datetime import datetime

def main():
  name = os.getenv('INPUT_NAME', 'Udacity Learner')

  print(f'Hello, {name}! Welcome to Continuous Integration.')
  timestamp = datetime.now().isoformat()
  print(f'Welcome logged at: {timestamp}')
  print(f'::set-output name=timestamp::{timestamp}')

if __name__ == '__main__':
  main()




'''
git init
git add .
git commit -m "First Commit"
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/CI-FullstackApp.git
git push -u origin main
'''
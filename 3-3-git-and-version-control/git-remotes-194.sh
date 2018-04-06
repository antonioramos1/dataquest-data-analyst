## 1. Introduction to Remote Repositories ##

/home/dq$ git clone /dataquest/user/git/chatbot

## 2. Making Changes to Cloned Repositories ##

/home/dq/chatbot$ git commit -m "Updated README.md"

## 3. Overview of the Master Branch ##

/home/dq/chatbot$ git status

## 4. Pushing Changes to the Remote ##

/home/dq/chatbot$ git push origin master

## 5. Viewing Individual Commits ##

/home/dq/chatbot$ git show 14a04302d0fd76e21ab9ad878b870dbbadabfb7e

## 6. Commits and the Working Directory ##

/home/dq/chatbot$ git diff 14a04302d0fd76e21ab9ad878b870dbbadabfb7e 4e3753bdb73c

## 7. Switching to a Specific Commit ##

/home/dq/chatbot$ git reset --hard 4e3753bdb73ce128740dd42eab7527ee49772994

## 8. Pulling From a Remote Repo ##

/home/dq/chatbot$ git pull

## 9. Referring to the Most Recent Commit ##

/home/dq/chatbot$ git reset --hard HEAD~1
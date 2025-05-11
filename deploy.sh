#!/bin/bash

# Define variables
APP_NAME="status-page-app" # Replace with your app name
POSTGRES_ADDON="heroku-postgresql:hobby-dev"

# Check if Heroku CLI is installed
if ! command -v heroku &> /dev/null
then
    echo "Heroku CLI not found. Please install it: https://devcenter.heroku.com/articles/heroku-cli"
    exit
fi

# Step 1: Login to Heroku
echo "Logging into Heroku CLI..."
heroku login

# Step 2: Create a new Heroku app
echo "Creating Heroku app..."
heroku create $APP_NAME

# Step 3: Add PostgreSQL addon to the app
echo "Adding PostgreSQL addon..."
heroku addons:create $POSTGRES_ADDON --app $APP_NAME

# Step 4: Set up environment variables
echo "Setting up environment variables..."
heroku config:set DATABASE_URL=$(heroku config:get DATABASE_URL --app $APP_NAME) --app $APP_NAME

# Step 5: Push code to Heroku
echo "Pushing code to Heroku..."
git init
heroku git:remote --app $APP_NAME
git add .
git commit -m "Deploying FastAPI app to Heroku"
git push heroku master

# Step 6: Run database migrations
echo "Running database migrations..."
heroku run python main.py --app $APP_NAME

# Step 7: Open the app
echo "Opening the app in your browser..."
heroku open --app $APP_NAME

echo "Deployment complete!"
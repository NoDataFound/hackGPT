`Slack Bot Setup`
Follow these steps to set up a Slack bot for your workspace:

- Log in to your Slack workspace.
- Go to the Slack API website.
- Click on `"Create an app"` and select `"From scratch"`.
- Give your app a name and select your Slack workspace.
- In the `Basic Information section`, click on:
  - `Add features and functionality`.
  - Then click on `Permissions`.

In the`Bot Token Scopes` section, add the following scopes:

```
app_mentions:read
channels:history
channels:read
chat:write
```
In the `Settings` section, click on `Socket Mode` and enable it. Give the token a name. Copy the `Slack Bot App Token` (starts with ```xapp```).

In the `Basic Information` section, click on `Add features and functionality` again. Then click on `Event Subscriptions` and enable it.

In the `Subscribe to bot events` section, select `app_mention`. Save the changes.

Go to the `OAuth & Permissions` section and install your app to your workspace.

Copy the `Slack Bot Token` (starts with ```xoxb```).

To run the Slack bot with Python 3, execute the following command in your terminal:

```
python3 chatbot.py
```
Make sure you have the required dependencies installed and replace chatbot.py with the filename of your bot script.
# Langchain Prompt Templates from Robocorp Asset Storage

Prompt Templates is a neat way of managing the prompts that go to large-language models, but keeping the templates in the code often means you'll need to redeploy your project for changes to take effect. Also, you might want different people to work on the prompt templates than actual code.

💡 **SOLUTION: Let's put the prompt templates to Robocorp Asset Storage!** 💡

Apart from being able to iterate the prompt templates fast, using Robocorp for developing and running Langchain workloads, you'll get several benefits.

- Curated collection of Python libraries built for automating typical sources of data for e.g. RAG data loaders (websites with Playwright, desktops legacy apps, any cloud platform, documents with OCR, excel and much more).
- Amazing environment control - define dependencies once, and tooling takes care of environment builds and a whole lot more when developing and running workflows.
- Run anywhere - Robocorp offers zero-infra workers in the cloud, or you can self-host on-demand containers, Windows VMs or dedicated machines on any (common) OS. Why this matters: your RAG data loaders can work where your data and apps are.

## Step-by-step

Follow this guide to get going. This assumes that you have not previously used Robocorp, so we go through everything step-by-step.

1️⃣ Install [VS Code](https://code.visualstudio.com/) (well, I bet you might have that already;)

2️⃣ Install [Robocorp Code extension](https://marketplace.visualstudio.com/items?itemName=robocorp.robocorp-code) - this one connects your dev environment with the Robocorp Control Room

3️⃣ Create a [Robocorp Control Room](https://cloud.robocorp.com) account - free accounts available, no credit card needed!

![image](https://github.com/tonnitommi/example-prompt-template-assets/assets/40179958/4f810d28-ea55-41c0-a4f8-148475d8c954)

4️⃣ In Control Room, create a Vault entry for OpenAI API credentials. Use the name `OpenAI` and `api-key` unless you want to edit the code.

![image](https://github.com/tonnitommi/example-prompt-template-assets/assets/40179958/32ce1c03-ae0c-4840-9e79-9d98af054c03)

![image](https://github.com/tonnitommi/example-prompt-template-assets/assets/40179958/ee533d47-dbdf-4fd1-9d3a-3dc7b63b7a06)

5️⃣ In Control Room, create an Asset for the prompt template. Use the name `example_prompt_template` unless you want to edit the code. The text is fully shown [here](prompt_template.txt) for easy copy pasting.

![image](https://github.com/tonnitommi/example-prompt-template-assets/assets/40179958/a174f7ac-db32-4b78-9dbe-6132f1c420fd)

![image](https://github.com/tonnitommi/example-prompt-template-assets/assets/40179958/73804534-306e-4383-a1d6-525fb240c04e)

6️⃣ Clone this example's Git repository to your own machine - use the way most familiar with you!

7️⃣ Open the cloned project folder in VS Code, our extension gets to work to automatically build the Python environment. It'll take a few minutes for the first time.

8️⃣ Hit Command Palette `Cmd-Shift-P` or `Win-Shift-P` and find `Robocorp: Run Robot`. Voila!

<img width="1389" alt="Screenshot 2023-09-19 at 13 56 54" src="https://github.com/tonnitommi/example-prompt-template-assets/assets/40179958/185caa66-885e-4d3d-a956-bd1c154683ae">













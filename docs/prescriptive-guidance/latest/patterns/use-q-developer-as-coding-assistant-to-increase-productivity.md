---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-q-developer-as-coding-assistant-to-increase-productivity.html
---

# Use Amazon Q Developer as a coding assistant to increase your productivity
<a name="use-q-developer-as-coding-assistant-to-increase-productivity"></a>

*Ram Kandaswamy, Amazon Web Services*

## Summary
<a name="use-q-developer-as-coding-assistant-to-increase-productivity-summary"></a>

This pattern uses a tic-tac-toe game to demonstrate how you can apply Amazon Q Developer across a range of development tasks. It generates code for a tic-tac-toe game as a single-page application (SPA), enhances its UI, and creates scripts to deploy the application on AWS.

Amazon Q Developer functions as a coding assistant to help accelerate software development workflows and enhance productivity for both developers and non-developers. Regardless of your technical expertise, it helps you create architectures and design solutions for business problems, bootstraps your working environment, helps you implement new features, and generates test cases for validation. It uses natural language instructions and AI capabilities to ensure consistent, high-quality code and to mitigate coding challenges regardless of your programming skills.

The key advantage of Amazon Q Developer is its ability to liberate you from repetitive coding tasks. When you use the `@workspace` annotation, Amazon Q Developer ingests and indexes all code files, configurations, and project structure in your integrated development environment (IDE), and provides tailored responses to help you focus on creative problem-solving. You can dedicate more time to designing innovative solutions and enhancing the user experience. If you aren't technical, you can use Amazon Q Developer to streamline workflows and collaborate more effectively with the development team. The Amazon Q Developer **Explain code** feature offers detailed instructions and summaries, so you can navigate complex code bases.

Furthermore, Amazon Q Developer provides a language-agnostic approach that helps junior and mid-level developers expand their skill sets. You can concentrate on core concepts and business logic instead of language-specific syntax. This reduces the learning curve when you switch technologies.

## Prerequisites and limitations
<a name="use-q-developer-as-coding-assistant-to-increase-productivity-prereqs"></a>

**Prerequisites**
+ IDE (for example, WebStorm or Visual Studio Code) with the Amazon Q Developer plugin installed. For instructions, see [Installing the Amazon Q Developer extension or plugin in your IDE](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE-setup.html) in the Amazon Q Developer documentation.
+ An active AWS account set up with Amazon Q Developer. For instructions, see [Getting started](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/getting-started-q-dev.html) in the Amazon Q Developer documentation.
+ **npm** installed. For instructions, see the [npm documentation](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm). This pattern was tested with npm version 10.8.
+ AWS Command Line Interface (AWS CLI) installed. For instructions, see the [AWS CLI documentation](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

**Limitations**
+ Amazon Q Developer can perform only one development task at a time.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.

## Tools
<a name="use-q-developer-as-coding-assistant-to-increase-productivity-tools"></a>
+ This pattern requires an IDE such as Visual Studio Code or WebStorm. For a list of supported IDEs, see the [Amazon Q Developer documentation](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE.html#supported-ides-features).
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open source tool that helps you interact with AWS services through commands in your command-line shell.

## Best practices
<a name="use-q-developer-as-coding-assistant-to-increase-productivity-best-practices"></a>

See [Best coding practices with Amazon Q Developer](https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-code-generation/best-practices-coding.html) in AWS Prescriptive Guidance. In addition:
+ When you provide prompts to Amazon Q Developer, make sure that your instructions are clear and unambiguous. Add code snippets and annotations such as `@workspace` to the prompt to provide more context for your prompts.
+ Include relevant libraries and import them to avoid conflicts or incorrect guesses by the system.
+ If the code generated isn't accurate or as expected, use the **Provide feedback & regenerate** option. Try breaking the prompts into smaller instructions.

## Epics
<a name="use-q-developer-as-coding-assistant-to-increase-productivity-epics"></a>

### Set up the working environment
<a name="set-up-the-working-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a new project. | To create a new project in your working environment, run the following command and accept the default settings for all questions:<pre>npx create-next-app@latest</pre> | App developer, Programmer, Software developer |
| Test the base application. | Run the following command and confirm that the base application loads successfully in the browser:<pre>npm run dev </pre> | App developer, Programmer, Software developer |
| Clean up the base code. | Navigate to the `page.tsx` file in the `src/app` folder and delete the default content to get a blank page. After deletion, the file should look like this:<pre>export default function Home() {<br />  return (<div></div><br />      );<br />}</pre> | App developer, Programmer, Software developer |

### Use Amazon Q Developer to design a tic-tac-toe game project
<a name="use-qdevlong-to-design-a-tic-tac-toe-game-project"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Get an overview of steps. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-q-developer-as-coding-assistant-to-increase-productivity.html) | App developer, Programmer, Software developer |
| Generate code for tic-tac-toe. | In the chat panel, start a development task by using the `/dev` command followed by the description of the task. For example:<pre>/dev Create a React-based single-page application  written in TypeScript for a tic-tac-toe game with the following specifications:<br />1. Design an aesthetically pleasing interface with the game grid centered vertically and <br />horizontally on the page. <br />2. Include a heading and clear instructions on how to play the game.<br />3. Implement color-coding for X and O marks to distinguish them easily. </pre><br />Amazon Q Developer generates code based on your instructions. | App developer, Programmer, Software developer |
| Inspect and accept the generated code. | Visually inspect the code, and choose **Accept code** to automatically replace the `page.tsx` file.<br />If you run into issues, choose **Provide feedback & regenerate** and describe the issue you encountered. | App developer, Programmer, Software developer |
| Fix lint errors. | The example tic-tac-toe game includes a grid. The code that Amazon Q Developer generates might use the default type `any`. You can add type safety by prompting Amazon Q Developer as follows:<pre>/dev Ensure proper TypeScript typing for the onSquare Click event handler <br />to resolve any 'any' type issues.</pre> | App developer, Programmer, Software developer |
| Add visual appeal. | You can break the original requirement into smaller fragments. For example, you can improve the game UI with the following prompts in the dev tasks. This prompt enhances Cascading Style Sheets (CSS) styles and exports the app for deployment.<pre>/dev Debug and fix any CSS issues to correctly display the game grid and overall layout. <br /><br />Simplify the code by removing game history functionality and related components. <br /><br />Implement static file export to an 'out' directory for easy deployment. The solution <br />should be fully functional, visually appealing, and free of typing errors or layout issues. </pre> | App developer, Programmer, Software developer |
| Test again. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-q-developer-as-coding-assistant-to-increase-productivity.html) | App developer, Programmer, Software developer |

### Deploy the application to the AWS Cloud
<a name="deploy-the-application-to-the-aws-cloud"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create folders and files for deployment. | In the project in your working environment, create a deployment folder and two files inside it: `pushtos3.sh` and `cloudformation.yml`:<pre>mkdir deployment && cd deployment<br />touch pushtos3.sh && chmod +x pushtos3.sh<br />touch cloudformation.yml</pre> | App developer, Programmer, Software developer |
| Generate automation code. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-q-developer-as-coding-assistant-to-increase-productivity.html) | AWS administrator, AWS DevOps, App developer |
| Generate script content. | To create a deployment script, use the following prompt:<pre>/dev Modify the pushtos3 shell script so that it can use AWS CLI commands to create a <br />CloudFormation stack named tictactoe-stack if it does not exist already, and use <br />cloudformation.yml as the source template. Wait for the stack to complete and sync the <br />contents from the out folder to the S3 bucket. Perform invalidation of the CloudFront <br />origin.</pre> | App developer, Programmer, Software developer |
| Deploy the application to the AWS Cloud. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-q-developer-as-coding-assistant-to-increase-productivity.html) | AWS administrator, AWS DevOps, Cloud architect, App developer |

## Troubleshooting
<a name="use-q-developer-as-coding-assistant-to-increase-productivity-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| The build doesn't create a single-page application or export it to the output folder. | Look at the contents of the `next.config.mjs` file.<br />If the code has the following default configuration:<pre>const nextConfig = {};</pre><br />modify it as follows:<pre>const nextConfig = {<br />  output: 'export',<br />  distDir: 'out',<br />};</pre> |

## Related resources
<a name="use-q-developer-as-coding-assistant-to-increase-productivity-resources"></a>
+ [Creating a new React project](https://react.dev/learn/start-a-new-react-project) (React documentation)
+ [Amazon Q Developer overview](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html) (AWS documentation)
+ [Amazon Q Developer best practices ](https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-code-generation/introduction.html)(AWS Prescriptive Guidance)
+ [Installing, configuring, and using Amazon Q Developer with JetBrains IDEs](https://www.youtube.com/watch?v=-iQfIhTA4J0&pp=ygUSYW1hem9uIHEgZGV2ZWxvcGVy) (YouTube video)
+ [Installing Amazon Q for the command line](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-getting-started-installing.html) (AWS documentation)

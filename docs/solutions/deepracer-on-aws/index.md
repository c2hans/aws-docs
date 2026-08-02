---
source_url: https://docs.aws.amazon.com//solutions/deepracer-on-aws//index.html
---

# DeepRacer on AWS

Developers of all skill levels can get hands on with machine learning through a 3D racing simulator and fully autonomous 1/18th scale race cars driven by reinforcement learning.

- **Version**: 1.2.5
- **Release**: 07/2026
- **Author**: AWS
- **Est. deployment time**: 30 mins
- **Estimated cost**: [See details](/solutions/latest/deepracer-on-aws/cost.html)

## Overview

With DeepRacer on AWS you'll learn fundamental concepts, skills, and machine learning (ML) training techniques that power foundation models in some of the most advanced generative AI applications today through the fun of racing autonomous cars. DeepRacer on AWS gives you a fun and hands-on way to learn to train ML models, where you can see your training come to life by deploying your model in a virtual racing environment or onto an autonomous RC car and miniature race track.

## Benefits

### Hands-on learning

DeepRacer on AWS transforms complex reinforcement learning concepts into an approachable, practical experience through its interactive, user-friendly platform. Users learn the fundamentals of reinforcement learning in a gamified setting without traditional barriers to entry. The platform provides immediate feedback through virtual or physical racing, creating an engaging learning loop that serves both beginners and advanced users.

### Experiment and grow

Test model training fundamentals using the DeepRacer on AWS 3D racing simulator. Experiment with multiple sensor inputs, the latest reinforcement learning algorithms, neural network configurations and simulation to-real domain transfer methods.

### Learn through competition

Once you have built your model, it's time to race! Compete against colleagues, host community races or create your own league to put your machine learning skills to the test.

## How it works

You can automatically deploy this architecture using the implementation guide and the accompanying AWS CloudFormation template. [View implementation guide](/solutions/latest/deepracer-on-aws/solution-overview.html)

![DeepRacer on AWS](/images/solutions/deepracer-on-aws/images/deepracer-architecture.png)

1. **Step 1**: A user accesses the DeepRacer on AWS user interface through an Amazon CloudFront distribution, which delivers static web assets from the UI assets bucket and video streams from simulations.
1. **Step 2**: The user interface assets are hosted in an Amazon S3 bucket that stores the static web assets comprising the user interface.
1. **Step 3**: An Amazon Cognito user pool manages users and user group membership.
1. **Step 4**: An Amazon Cognito identity pool manages federation and rule-based role mapping for users.
1. **Step 5**: AWS Identity and Access Management roles define permissions and level-of-access for each user group in the system, used for access control and authorization.
1. **Step 6**: AWS Lambda registration hooks execute pre- and post-registration actions including assigning new users as racers, handling initial admin profile creation, and more.
1. **Step 7**: AWS WAF provides intelligent protection for the API against common attack vectors and allows customers to define custom rules based on individual use cases and usage patterns.
1. **Step 8**: Amazon API Gateway routes API requests to their appropriate handler using a defined Smithy model.
1. **Step 9**: A single Amazon DynamoDB table is responsible for storing and managing profiles, training jobs, models, evaluation jobs, submissions, and leaderboards.
1. **Step 10**: AWS Lambda functions are triggered in response to requests routed from the API and are responsible for CRUD operations, dispatching training/evaluation jobs, and more.
1. **Step 11**: A global settings handler (AWS Lambda function) reads and writes application-level settings to the configuration.
1. **Step 12**: An AWS AppConfig hosted configuration stores application-level settings, such as usage quotas.
1. **Step 13**: Model export handlers (AWS Lambda functions) retrieve the asset URL and package assets for use in exporting models from the system.
1. **Step 14**: An Amazon Simple Queue Service dead-letter queue catches failed export jobs from the asset packaging function.
1. **Step 15**: A virtual model bucket stores exported models and provides access to them via pre-signed URL.
1. **Step 16**: A model import handler (AWS Lambda function) receives requests to import a model onto the system and creates a new import job.
1. **Step 17**: A model import queue (Amazon Simple Queue Service) receives jobs from the model import function and holds them until they are accepted by the dispatcher; a DLQ handles failed jobs.
1. **Step 18**: A failed request handler (AWS Lambda function) manages failed requests and updates their status to reflect their current state.
1. **Step 19**: An import dispatching function takes a job from the queue and dispatches it to the workflow.
1. **Step 20**: A reward function validator (AWS Lambda function) checks the reward function and validates/sanitizes the customer-provided code before it is saved to the system.
1. **Step 21**: An imported model validator function checks and validates the imported model before it is saved to the system.
1. **Step 22**: An imported model assets handler (AWS Lambda function) brings in model assets from the upload bucket.
1. **Step 23**: An import completion handler (AWS Lambda function) handles status updates when a job is completed successfully.
1. **Step 24**: An upload bucket (Amazon S3) stores uploaded (but not yet imported) assets from the user.
1. **Step 25**: An Amazon Simple Queue Service FIFO queue receives requests for training and evaluation jobs and stores them in FIFO order.
1. **Step 26**: A job dispatcher function picks a job off the top of the FIFO queue and dispatches it to the workflow.
1. **Step 27**: Workflow functions handle setting up the job, setting status, and other workflow tasks.
1. **Step 28**: Amazon SageMaker AI training jobs perform the actual training and evaluation of the model using the reward function and hyperparameters provided.
1. **Step 29**: Amazon Kinesis Video Streams handles presenting the simulation video to the user from the training job.
1. **Step 30**: A user data bucket stores all user data including trained models, evaluation results, and other assets generated during the DeepRacer workflow.
1. **Step 31**: An Amazon DynamoDB stream captures table changes to trigger the live race orchestration and real-time broadcasting pipelines.
1. **Step 32**: A broadcast handler (AWS Lambda function) processes stream records, detects relevant state changes, builds typed events, and publishes them to the real-time messaging channel.
1. **Step 33**: AWS IoT Core provides a managed MQTT message broker that delivers real-time race state updates to spectator and participant browsers via authenticated WebSocket connections.
1. **Step 34**: An Amazon EventBridge rule triggers the SafetyNet function whenever a live race workflow execution reaches a terminal state, ensuring the execution lock is cleared and pending evaluations are retriggered without manual intervention.
1. **Step 35**: Queue API handlers (AWS Lambda functions) handle race facilitator operations including reorder, remove, reset, clear leaderboard, launch race, and declare winner.
1. **Step 36**: An attach IoT policy function (AWS Lambda) resolves the caller's identity and attaches the messaging policy, authorizing real-time subscriptions for live race viewing.
1. **Step 37**: A stream handler (AWS Lambda function) monitors the stream for new or pending queue items, verifies race preconditions, acquires the execution lock, and starts the evaluation workflow.
1. **Step 38**: A SafetyNet function (AWS Lambda) serves as an execution recovery handler that clears the execution lock, applies backoff logic for repeated failures, and retriggers the stream handler if items remain in the queue.
## Deploy with confidence

Everything you need to launch this AWS Solution in your account is right here.

- **We'll walk you through it**: Get started fast. Read the implementation guide for deployment steps, architecture details, cost information, and customization options.

[Open guide](/solutions/latest/deepracer-on-aws/solution-overview.html)

- **Let's make it happen**: Ready to deploy? Follow a step-by-step guide in the AWS Console to begin setting up the infrastructure you need. You'll be prompted to access your AWS account if you haven't yet logged in.

[AWS Launch Wizard](https://us-east-1.console.aws.amazon.com/launchwizard/home?region=us-east-1&redirectId=SolutionWeb#/deployment/create/SO0310)

## Deployment tools

Follow these links for direct access to the artifacts for this AWS Solution.

- **CloudFormation template**: View or modify the CloudFormation template to customize your deployment.

[Download template](https://s3.amazonaws.com/solutions-reference/deepracer-on-aws/latest/deepracer-on-aws.template)

- **Source code**: The source code for this AWS Solution is available in GitHub.

[Go to GitHub](https://github.com/aws-solutions/deepracer-on-aws)

- **Implementation guide**: Follow the implementation guide for step-by-step actions to deploy this AWS Solution.

[Download guide](https://docs.aws.amazon.com/pdfs/solutions/latest/deepracer-on-aws/deepracer-on-aws.pdf)

## Related content

- **Amazon DeepRacer Chatbot**: This Guidance illustrates how to deploy and use the AWS DeepRacer Chatbot, an intelligent virtual assistant powered by multimodal generative AI and domain adaptation techniques.

[Go to Guidance](https://aws.amazon.com/solutions/guidance/deploying-an-aws-deepracer-chatbot/)

- **Training an AWS DeepRacer Model using Amazon SageMaker AI**: This Guidance demonstrates how software developers can use an Amazon SageMaker AI Notebook instance to directly train and evaluate AWS DeepRacer models with full control.

[Go to Guidance](https://aws.amazon.com/solutions/guidance/training-an-aws-deepracer-model-using-amazon-sagemaker/)

- **AWS DeepRacer Event Management**: This Guidance demonstrates how to deploy and configure DeepRacer Event Manager (DREM), a set of tools that simplify the hosting of AWS DeepRacer events.

[Go to Guidance](https://aws.amazon.com/solutions/guidance/aws-deepracer-event-management/)

## Customer stories

### TOPAZ

"As a fintech headquartered outside the São Paulo metropolitan area, recruiting specialized talent is one of our biggest challenges. Using DeepRacer on AWS, we partnered with local university FATEC to deliver a hands-on AI experience to over 160 students during our Technology Week. The event strengthened our talent pipeline and reinforced our commitment to developing the local tech ecosystem — a virtuous cycle where education fuels innovation."

**Rangel Graçadio, CTO**

---

## AWS Support

- [Get support for this AWS Solution](/solutions/latest/deepracer-on-aws/contact-aws-support.html)

## RSS Feed

- [Subscribe now to get updates on the latest release.](https://solutions-reference.s3.us-east-1.amazonaws.com/deepracer-on-aws/latest/rss.xml)

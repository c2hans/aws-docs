---
source_url: https://docs.aws.amazon.com//solutions/deepracer-on-aws//index.html
---

---
title: 'DeepRacer on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/deepracer-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# DeepRacer on AWS

Developers of all skill levels can get hands on with machine learning through a 3D racing simulator and fully autonomous 1/18th scale race cars driven by reinforcement learning.

- **Version**: 1.3.2
- **Release**: 10/2026
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

1. **Step 1**: A user accesses the DeepRacer on AWS user interface through an Amazon CloudFront distribution, which delivers the static web assets from the UI assets bucket.
1. **Step 2**: The user interface assets are hosted in an Amazon S3 bucket that stores the static web assets comprising the user interface.
1. **Step 3**: An Amazon Cognito user pool manages users and user group membership.
1. **Step 4**: An Amazon Cognito identity pool manages federation and authorization.
1. **Step 5**: AWS Identity and Access Management user group roles define permissions and levels of access for each type of user in the system, used for access control and authorization.
1. **Step 6**: AWS Lambda Cognito trigger functions run at points in the user lifecycle, such as sign-up, confirmation, and outgoing email. The pre-signup trigger applies new-user limits and creates the profile, and the post-confirmation trigger assigns the default racer group.
1. **Step 7**: AWS WAF provides intelligent protection for the API against common attack vectors and allows customers to define custom rules based on individual use cases and usage patterns.
1. **Step 8**: Amazon API Gateway routes API requests to their appropriate handler using a defined Smithy model.
1. **Step 9**: An Amazon DynamoDB table serves as a single table for storing and managing profiles, training jobs, models, evaluation jobs, submissions, leaderboards, events, tracks, runs, laps, rankings, fleets, devices, and deployments.
1. **Step 10**: AWS Lambda API functions back the API, with one function per operation. One function backs each API operation, covering profiles, models, races, events, devices, model import and export, and global settings.
1. **Step 11**: AWS AppConfig hosted configuration stores application-level settings, such as usage quotas.
1. **Step 12**: A user data bucket (Amazon S3) stores all user data including trained models, evaluation results, and other assets generated during the DeepRacer workflow.
1. **Step 13**: An asset packaging AWS Lambda function packages a model's assets from the user data bucket into the virtual model bucket for export. Packaging jobs that fail go to an Amazon Simple Queue Service dead-letter queue.
1. **Step 14**: A virtual model bucket (Amazon S3) stores exported models. The user's browser downloads an exported model directly from this bucket using the pre-signed URL the API returns.
1. **Step 15**: An Amazon Simple Queue Service FIFO queue receives requests for training and evaluation jobs and stores them in FIFO order. A job that repeatedly fails to dispatch moves to a dead-letter queue rather than blocking the jobs behind it.
1. **Step 16**: An AWS Step Functions training workflow runs each training or evaluation job from start to finish. If no training capacity is available it cleans up and leaves the job waiting for capacity. Otherwise it polls the job every minute while it runs, and finalizes the job whether it succeeds or fails.
1. **Step 17**: AWS Lambda workflow functions perform the steps of each job. They dispatch each job, set it up, start and monitor the SageMaker job, and record the result.
1. **Step 18**: Amazon SageMaker AI performs the actual training and evaluation of the model using the reward function and hyperparameters provided. Each job runs the DeepRacer training container image from Amazon ECR.
1. **Step 19**: Amazon Kinesis Video Streams carries the simulation video from the SageMaker job to the user's browser.
1. **Step 20**: An Amazon DynamoDB Stream captures item-level changes from the main table and delivers them to the race functions, enabling event-driven orchestration of live race evaluations and real-time broadcast of race state to spectators.
1. **Step 21**: AWS Lambda race functions respond to live and physical race activity. They start each race evaluation, broadcast race state, recover stalled executions, and rebuild race statistics.
1. **Step 22**: An AWS Step Functions live race workflow runs the queued submissions for a live race one at a time. The stream handler or a facilitator launching the race starts it. For each submission it runs the evaluation on SageMaker through the workflow functions, using four functions of its own:
1. **Step 23**: Amazon EventBridge routes race events.
1. **Step 24**: AWS IoT Core provides a managed WebSocket pub/sub channel for delivering live race state updates to spectator and participant browsers. Each live race uses a dedicated MQTT topic scoped by leaderboard ID, physical race events use a per-event topic tree, and device status and command results go to the device management screens. Browsers subscribe via WebSocket, and the broadcast handler publishes via IAM-authorized HTTPS, so no connections table or custom connect and disconnect handlers are needed. Facilitator and administrator browsers also publish directly to IoT Core, sending race countdown, pause, and resume state and race topic updates without passing through Lambda, which keeps timing jitter low.
1. **Step 25**: An Amazon Simple Queue Service event delete queue receives a cascade-delete request when an event is deleted, so dependent records are removed asynchronously rather than inside the API request. Requests that keep failing go to a dead-letter queue for manual re-drive.
1. **Step 26**: An event delete worker AWS Lambda function consumes the delete queue and removes the laps, runs, rankings, submissions, and tracks belonging to a deleted event, then the event record itself. It takes one message per invocation and is capped at two concurrent executions, so at most two events are torn down at a time.
1. **Step 27**: AWS Systems Manager provides the hybrid activation that enrolls physical cars and timers as managed instances, and RunCommand for running commands on them. Each device is addressed by the managed instance id that hybrid activation assigned to it.
1. **Step 28**: Physical devices (cars and timers) enroll themselves as managed instances using a hybrid activation code, and receive model deployments and control commands through Systems Manager. When a model is deployed, the car downloads it directly from the user data bucket using a pre-signed URL included in the command.
1. **Step 29**: Amazon EventBridge device rules keep device status current.
1. **Step 30**: AWS Lambda device functions track the state of each device. They track device registration, poll device status, and deregister devices whose records have expired.
1. **Step 31**: Amazon GuardDuty malware protection scans physical models uploaded to the upload bucket and tags each object with the result. The model optimizer polls for that tag for up to a minute and proceeds only when the scan found no threats. A detected threat, an unscannable file, and a scan that failed or never reported all stop the import with a message instead. Malware scanning is on by default, and setting the ENABLE_GUARDDUTY_MALWARE_SCAN=false CDK context value at synthesis time leaves it out, after which the optimizer no longer waits for a tag.
1. **Step 32**: AWS Lambda model transfer functions prepare a model for a physical car and deliver it. The optimizer converts a model into the format a physical car requires, and the push functions send the transfer command and track its status.
1. **Step 33**: An AWS Step Functions push workflow orchestrates transferring a model to a physical car. It marks the deployment in progress, sends the download and installation command to the car through Systems Manager RunCommand along with a pre-signed URL for the model in the user data bucket, polls until the command finishes, and records the deployment as completed or failed.
1. **Step 34**: An upload bucket (Amazon S3) stores uploaded (but not yet imported) assets from the user.
1. **Step 35**: An Amazon Simple Queue Service import queue receives import jobs from the API functions and holds them until they are accepted by the import dispatcher. Jobs that fail twice move to a dead-letter queue, where a handler marks the import as failed.
1. **Step 36**: An AWS Step Functions import workflow validates an imported virtual model and brings it into the system. It validates the reward function, validates the model, imports the model assets, and records the import as complete, stopping at the first validation that fails.
1. **Step 37**: AWS Lambda import functions perform the steps of each import. They dispatch each import, validate the reward function and the model, copy the assets, and record the outcome.
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

- **Custom OS installation on AWS DeepRacer devices**: Learn how to upgrade or install a custom operating system on your AWS DeepRacer device using a newly released developer bootloader, extending the life of your hardware with modern Linux distributions and custom software stacks.

[Read blog post](https://aws.amazon.com/blogs/machine-learning/custom-os-installation-now-available-on-aws-deepracer-devices/)

- **Building a custom car for AWS DeepRacer**: Explore how to build a modern AWS DeepRacer replacement using off-the-shelf components, with step-by-step guidance for constructing your own autonomous racing car.

[Read on Builder](https://builder.aws.com/content/3CzhcPjj9cJE37Ft4j8JUWX5A5U/building-a-modern-aws-deepracer-replacement-using-off-the-shelf-components-part-1)

- **Amazon DeepRacer Chatbot**: This Guidance illustrates how to deploy and use the AWS DeepRacer Chatbot, an intelligent virtual assistant powered by multimodal generative AI and domain adaptation techniques.

[Go to Guidance](https://aws.amazon.com/solutions/guidance/deploying-an-aws-deepracer-chatbot/)

- **Training an AWS DeepRacer Model using Amazon SageMaker AI**: This Guidance demonstrates how software developers can use an Amazon SageMaker AI Notebook instance to directly train and evaluate AWS DeepRacer models with full control.

[Go to Guidance](https://aws.amazon.com/solutions/guidance/training-an-aws-deepracer-model-using-amazon-sagemaker/)

- **AWS DeepRacer Event Management**: This Guidance demonstrates how to deploy and configure DeepRacer Event Manager (DREM), a set of tools that simplify the hosting of AWS DeepRacer events.

[Go to Guidance](https://aws.amazon.com/solutions/guidance/aws-deepracer-event-management/)

## Customer stories

### ACADEMIA DE INVENTORES

"At Academia de Inventores, our mission is to make AI education accessible to every student in Spain. As the educational delivery partner for the AWS Futuro IA program, we are organizing the country's first National Student Championship using DeepRacer on AWS, in collaboration with the Gobierno de Aragón through their Campus Digital initiative. With just an internet connection, thousands of students from high school, vocational training, and university train their own reinforcement-learning models, progressing from virtual qualifiers to a live national final in Aragón. DeepRacer turns AI from an abstract concept into a hands-on, competitive experience reaching every region of Spain. When you give a 16-year-old the power to train an AI model and compete nationally, you're not just teaching a skill, you're igniting a vocation."

**Luis Martin, Founder & CEO**

### TOPAZ

"As a fintech headquartered outside the São Paulo metropolitan area, recruiting specialized talent is one of our biggest challenges. Using DeepRacer on AWS, we partnered with local university FATEC to deliver a hands-on AI experience to over 160 students during our Technology Week. The event strengthened our talent pipeline and reinforced our commitment to developing the local tech ecosystem — a virtuous cycle where education fuels innovation."

**Rangel Graçadio, CTO**

---

## AWS Support

- [Get support for this AWS Solution](/solutions/latest/deepracer-on-aws/contact-aws-support.html)

## RSS Feed

- [Subscribe now to get updates on the latest release.](https://solutions-reference.s3.us-east-1.amazonaws.com/deepracer-on-aws/latest/rss.xml)

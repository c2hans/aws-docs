---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

This section provides an overview of the architecture of this solution.

 **Topics**
+  [Architecture diagram](#architecture-diagram)
+  [Architectural components](#architecture-components)
+  [Functional components](#functional-overview)
+  [AWS services](#aws-services-in-this-solution)

## Architecture diagram
<a name="architecture-diagram"></a>

Deploying this solution with the default parameters deploys the following components in your AWS account.

![Architecture diagram showing DeepRacer on AWS components including AWS IoT Core for live race real-time data delivery](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/architecture-diagram.png)

## Architectural components
<a name="architecture-components"></a>

1. A user accesses the DeepRacer on AWS user interface through an [Amazon CloudFront](https://aws.amazon.com/cloudfront/) distribution, which delivers static web assets from the UI assets bucket and video streams from simulations.

1. The user interface assets are hosted in an [Amazon S3](https://aws.amazon.com/s3/) bucket that stores the static web assets comprising the user interface.

1. An [Amazon Cognito](https://aws.amazon.com/cognito/) user pool manages users and user group membership.

1. An Amazon Cognito identity pool manages federation and rule-based role mapping for users.

1.  [AWS IAM](https://aws.amazon.com/iam/) roles define permissions and level-of-access for each user group in the system, used for access control and authorization.

1.  [AWS Lambda](https://aws.amazon.com/lambda/) registration hooks execute pre- and post-registration actions including assigning new users as racers, handling initial admin profile creation, and more.

1.  [AWS WAF](https://aws.amazon.com/waf/) provides intelligent protection for the API against common attack vectors and allows customers to define custom rules based on individual use cases and usage patterns.

1.  [Amazon API Gateway](https://aws.amazon.com/api-gateway/) routes API requests to their appropriate handler using a defined Smithy model.

1. A single [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) table is responsible for storing and managing profiles, training jobs, models, evaluation jobs, submissions, leaderboards, and the physical event entities (events, tracks, runs, and laps).

1. AWS Lambda functions are triggered in response to requests routed from the API and are responsible for CRUD operations, dispatching training/evaluation jobs, servicing the physical event endpoints (event lifecycle, tracks, runs, laps, statistics, and the combined leaderboard), and more.

1. A global settings handler (AWS Lambda function) reads and writes application-level settings to the configuration.

1. An [AWS AppConfig](https://aws.amazon.com/systems-manager/features/appconfig/) hosted configuration stores application-level settings, such as usage quotas.

1. Model export handlers (AWS Lambda functions) retrieve the asset URL and package assets for use in exporting models from the system.

1. An [Amazon SQS](https://aws.amazon.com/sqs/) dead-letter queue catches failed export jobs from the asset packaging function.

1. A virtual model bucket stores exported models and provides access to them via pre-signed URL.

1. A model import handler (AWS Lambda function) receives requests to import a model onto the system and creates a new import job.

1. A model import queue (Amazon SQS) receives jobs from the model import function and holds them until they are accepted by the dispatcher; a DLQ handles failed jobs.

1. A failed request handler (AWS Lambda function) manages failed requests and updates their status to reflect their current state.

1. An import dispatching function takes a job from the queue and dispatches it to the workflow.

1. A reward function validator (AWS Lambda function) checks the reward function and validates/sanitizes the customer-provided code before it is saved to the system.

1. An imported model validator function checks and validates the imported model before it is saved to the system.

1. An imported model assets handler (AWS Lambda function) brings in model assets from the upload bucket.

1. An import completion handler (AWS Lambda function) handles status updates when a job is completed successfully.

1. An upload bucket (Amazon S3) stores uploaded (but not yet imported) assets from the user.

1. An Amazon SQS FIFO queue receives requests for training and evaluation jobs and stores them in FIFO order.

1. A job dispatcher function picks a job off the top of the FIFO queue and dispatches it to the workflow.

1. Workflow functions handle setting up the job, setting status, and other workflow tasks.

1.  [Amazon SageMaker AI training jobs](https://aws.amazon.com/sagemaker/) perform the actual training and evaluation of the model using the reward function and hyperparameters provided.

1.  [Amazon Kinesis Video Streams](https://aws.amazon.com/kinesis/video-streams/) handles presenting the simulation video to the user from the training job.

1. A user data bucket (Amazon S3) stores all user data including trained models, evaluation results, and other assets generated during the DeepRacer workflow.

1.  [Amazon DynamoDB Streams](https://aws.amazon.com/dynamodb/) captures item-level changes from the main table and delivers them to downstream Lambda consumers, enabling event-driven orchestration of live race evaluations, real-time broadcast of race state to spectators, and recomputation of combined leaderboards for multi-track physical events.

1. A live broadcast handler (AWS Lambda function) is triggered by the DynamoDB stream. It detects relevant state changes, such as evaluation started or completed, leaderboard updates, and winner declarations, and publishes corresponding events to the IoT Core MQTT topic for the active race, delivering real-time updates to connected spectator browsers. For physical events, when a racer’s ranking changes on a track that belongs to an event, this handler also recomputes that event’s combined leaderboard using the event’s configured scoring strategy. The combined-leaderboard recomputation runs in an isolated failure path, so per-track leaderboard broadcast continues uninterrupted even if the aggregation fails.

1.  [AWS IoT Core](https://aws.amazon.com/iot/) provides a managed WebSocket pub/sub channel for delivering live race state updates to spectator and participant browsers. Each live race uses a dedicated MQTT topic scoped by leaderboard ID. Spectators subscribe via WebSocket. The broadcast handler publishes via IAM-authorized HTTPS. IoT Core handles connection management, fan-out, and scaling without requiring a connections table or custom connect/disconnect handlers. Physical events use a second topic per track, scoped by leaderboard ID, that carries countdown timer state and pause/resume signals to spectator displays. The race facilitator’s browser publishes to this topic directly rather than through the API, which keeps the countdown on venue displays synchronized with the facilitator’s own timer when a run is paused or resumed.

1.  [Amazon EventBridge (Rules)](https://aws.amazon.com/eventbridge/) triggers the SafetyNet Lambda whenever a live race Step Functions execution reaches a terminal state (succeeded, failed, aborted, or timed out), ensuring the execution lock is cleared and pending evaluations are retriggered without manual intervention.

1. Live race queue API handlers (AWS Lambda functions) back the live race queue management endpoints, handling facilitator operations including listing the queue, reordering submissions via fractional indexing, removing submissions, resetting in-progress or failed models, clearing the leaderboard, launching the live race, and declaring a winner.

1. An attach IoT policy handler (AWS Lambda function) grants newly authenticated users the IoT Core policy required to subscribe to live race MQTT topics over WebSocket, enabling real-time race state delivery to their browser sessions.

1. A stream handler (AWS Lambda function) is triggered by the DynamoDB stream and auto-starts a new Step Functions execution for a live race when one or more submissions with pending status exist in the queue, the race is in progress, autolaunch is enabled, and no execution is currently running. It acquires the execution lock via a conditional write before starting the execution.

1. A SafetyNet (AWS Lambda function) is invoked by EventBridge when a live race Step Functions execution reaches any terminal state. It clears the execution lock with a conditional write, applies a backoff check if the execution has failed repeatedly, and touches a pending queue item to generate a DynamoDB stream event — retriggering the stream handler to start a new execution if items remain in the queue.

1. An event deletion queue (Amazon SQS) receives the identifier of an event that an admin has deleted, so that removing the event’s child records runs asynchronously instead of holding open the API response. A dead-letter queue captures any message that fails after three attempts.

1. A cascade delete event handler (AWS Lambda function) consumes the event deletion queue. It removes the event’s child records, which are the laps, runs, rankings, submissions, and tracks, before removing the event itself. Deleting the deepest records first and the event record last means an interrupted deletion can safely restart from the beginning.

1. A model optimizer (AWS Lambda function packaged as a container image) converts a trained or imported model into the car-ready formats needed to run on a physical DeepRacer car.

1. A physical model import path scans an uploaded model archive for malware and then optimizes it before the model becomes available for deployment to a car.

1.  [Amazon GuardDuty](https://aws.amazon.com/guardduty/) automatically scans physical-model uploads for malware before the model optimizer converts them.

1. A push workflow ([AWS Step Functions](https://aws.amazon.com/step-functions/)) delivers an optimized model to a physical car through [AWS Systems Manager](https://aws.amazon.com/systems-manager/) and tracks the delivery status.

1. An optimized model bucket (Amazon S3) stores the car-ready model artifacts that the model optimizer produces.

## Functional components
<a name="functional-overview"></a>

This solution implements a serverless, microservices-based architecture that enables users to train and evaluate reinforcement learning models for autonomous racing. The architecture is organized around several key functional areas that work together to provide a complete reinforcement learning education platform.

Users access DeepRacer on AWS through a web-based console delivered via Amazon CloudFront, which provides fast, global distribution of the user interface assets. These static web assets are hosted in Amazon S3, ensuring reliable and scalable content delivery to users worldwide. Amazon Cognito manages user authentication and authorization, handling user registration, login, and session management.

When new users register, the system automatically creates user profiles and establishes proper permissions, ensuring a seamless onboarding experience. This authentication layer secures access to the platform while enabling users to maintain their own private workspace for models, training data, and race submissions.

All user interactions with the system flow through Amazon API Gateway, which serves as the central entry point for backend operations. The API Gateway routes requests to appropriate AWS Lambda functions based on the endpoint accessed, providing a clean separation between the user interface and backend processing logic. AWS WAF protects the API layer from common security threats such as bot attacks, DDoS attempts, and malicious traffic patterns.

The solution uses a combination of Amazon DynamoDB and Amazon S3 to handle different types of data storage needs. DynamoDB serves as the primary database for structured data including user profiles, model metadata, training job status, leaderboards, race submissions, and the records that describe physical racing events and their results. Amazon S3 handles file storage for larger assets such as trained model files, training logs, evaluation videos, and other user-generated content.

Alongside virtual racing, the solution supports running physical racing events, the kind held at a summit, a classroom, or a community meetup, where real vehicles run on a real track. An event is the container for everything about one such occasion: its format and scoring rules, the tracks it runs on, and the results it produces. An event moves through a defined sequence of states as it is configured, opened, run, and closed, and each state limits what can still be changed.

An event can run up to 10 tracks at once, which lets a large venue operate concurrent heats. Each track keeps its own leaderboard and can be operated independently by a different race facilitator. When an event is configured with a combined scoring strategy, the solution also maintains an aggregated leaderboard that ranks racers across every track they have raced.

During the event, a race facilitator uses the timekeeping interface to run each racer’s attempt. Individual laps are stored as separate records. This allows a facilitator to mark a single lap invalid, excluding a false trigger from the racer’s score, without disturbing the rest of the run. Administrators can additionally correct a recorded lap time. The solution preserves the original value and records who made the change, when, and why.

Two independent real-time paths keep displays current. Leaderboard changes travel from DynamoDB through the broadcast handler to AWS IoT Core. Countdown timer state travels from the facilitator’s browser to IoT Core directly, which is what keeps a paused timer on a venue display in step with the facilitator’s own screen.

The core reinforcement learning functionality is centered around Amazon SageMaker AI training jobs, which provides the compute resources for running reinforcement learning training and evaluation jobs. When users initiate training jobs, the requests are queued in Amazon SQS to manage demand and ensure fair resource allocation. AWS Step Functions orchestrates the workflow of preparing training environments, monitoring job progress, and handling completion tasks. The system pulls a containerized simulation environment from Amazon ECR, which comprises the DeepRacer virtual simulator built on robotics simulation technology.

During model training and evaluation, Amazon Kinesis Video Streams captures video from the simulation environment and streams it in real-time to the console. This allows users to watch their models learn and perform, providing immediate visual feedback on training progress and model behavior. The streaming capability delivers an engaging, visual experience that helps users understand how their models are developing and performing on the virtual race track.

During live race events, AWS IoT Core supplements the video stream by delivering real-time race state updates to spectator and participant browsers via a managed WebSocket connection. As each model evaluation completes, a Lambda function publishes leaderboard changes, queue status updates, and participant notifications to an IoT Core topic, which fans the events out to all connected clients instantly. This two-channel architecture keeps the high-bandwidth video traffic on Kinesis Video Streams while routing lightweight event data through IoT Core, ensuring both streams remain responsive under concurrent viewer load.

Before any user-provided code executes in the system, it passes through validation functions. These examine reward functions and imported models for security issues, ensuring that malicious or harmful code cannot compromise the system. The functions operate within isolated network environments that prevent external communication, providing an additional security boundary.

Amazon CloudWatch provides comprehensive monitoring and logging across all system components, collecting metrics, logs, and performance data from Lambda functions, SageMaker instances, API Gateway, and other services. This enables cloud administrators to understand system performance, troubleshoot issues, and optimize resource usage.

## AWS services
<a name="aws-services-in-this-solution"></a>

| AWS service | Function | Description |
| --- | --- | --- |
|  [Amazon API Gateway](https://aws.amazon.com/api-gateway/)  | Core | Hosts REST API endpoints in the solution. |
|  [AWS CloudFormation](https://aws.amazon.com/cloudformation/)  | Core | Used to deploy the solution. |
|  [Amazon CloudFront](https://aws.amazon.com/cloudfront/)  | Core | Serves the web content hosted in Amazon S3. |
|  [Amazon Cognito](https://aws.amazon.com/cognito/)  | Core | Handles user management and authentication for the API. |
|  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)  | Core | Stores all user data related to user profiles, models, leaderboards, submissions, and physical racing events in a single table. |
|  [Amazon Elastic Container Registry](https://aws.amazon.com/ecr/)  | Core | Stores the Simulation Application (SimApp) image as a public container image, which is used by SageMaker instances to run the DeepRacer simulation application. |
|  [Amazon GuardDuty](https://aws.amazon.com/guardduty/)  | Core | Automatically scans physical-model uploads for malware before they are optimized for car deployment. |
|  [Amazon Kinesis Video Streams](https://aws.amazon.com/kinesis/video-streams/)  | Core | Streams videos from SageMaker AI training jobs to the user console, providing real-time visual feedback of model performance. |
|  [AWS IoT Core](https://aws.amazon.com/iot/)  | Core | Provides a managed WebSocket pub/sub channel for delivering real-time race state updates (leaderboard changes, evaluation progress, and participant notifications) to spectator browsers during live race events, and countdown timer state to spectator displays during physical events. |
|  [Amazon S3](https://aws.amazon.com/s3/)  | Core | Hosts static web assets for the user console and stores user-generated artifacts such as model files, training logs, and evaluation videos. |
|  [Amazon SageMaker](https://aws.amazon.com/sagemaker/)  | Core | Runs the Simulation Application (SimApp) for training and evaluating DeepRacer models. |
|  [Amazon SQS](https://aws.amazon.com/sqs/)  | Core | Provides a first-in-first-out job queue that holds simulation jobs before they are forwarded to the job dispatcher, and a queue that defers the removal of a deleted physical event’s records to a background worker. |
|  [AWS Lambda](https://aws.amazon.com/lambda/)  | Core | Powers various functions including API request handling, model validation, reward function validation, job dispatching, and workflow management. |
|  [AWS Step Functions](https://aws.amazon.com/step-functions/)  | Core | Manages workflow functions that orchestrate training and evaluation jobs on SageMaker instances, and runs the push workflow that delivers optimized models to physical cars. |
|  [AWS WAF](https://aws.amazon.com/waf/)  | Core | Provides system protection against bot spam, DDoS attacks, credential stuffing, and other common attack vectors. |
|  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)  | Core | Provides monitoring and logging capabilities for all components of the DeepRacer on AWS solution. |
|  [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/)  | Core | Manages access control and permissions for various components of the DeepRacer on AWS solution. |
|  [Amazon Virtual Private Cloud (VPC)](https://aws.amazon.com/vpc/)  | Optional | Can be used to provide network isolation for SageMaker AI training jobs for enhanced security. |

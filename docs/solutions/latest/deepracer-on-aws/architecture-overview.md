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

The diagram groups components by feature and shows only the connections between those groups and the shared services. Where a group runs a workflow or a set of functions behind a single icon, the matching entry describes what that icon covers. Every group reads and writes the DynamoDB table, which the diagram notes beside the table rather than drawing a line from each group. A deployment-time [AWS CodeBuild](https://aws.amazon.com/codebuild/) project copies container images from public repositories into private [Amazon ECR](https://aws.amazon.com/ecr/) repositories in your account, and the components marked with the Amazon ECR icon run from those images. When you deploy this solution, it provisions the following components:

1. A user accesses the DeepRacer on AWS user interface through an [Amazon CloudFront](https://aws.amazon.com/cloudfront/) distribution, which delivers the static web assets from the UI assets bucket.

1. The user interface assets are hosted in an [Amazon S3](https://aws.amazon.com/s3/) bucket that stores the static web assets comprising the user interface.

   1. The same bucket holds a public leaderboard JSON object for each live race. Adding a track to an event writes an empty placeholder, the race functions rewrite it as rankings change, and CloudFront serves it to spectators on a short cache time to live (TTL) so standings are not shown stale.

1. An [Amazon Cognito](https://aws.amazon.com/cognito/) user pool manages users and user group membership.

1. An Amazon Cognito identity pool manages federation and authorization.

1.  [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) user group roles define permissions and levels of access for each type of user in the system, used for access control and authorization.

1.  [AWS Lambda](https://aws.amazon.com/lambda/) Cognito trigger functions run at points in the user lifecycle, such as sign-up, confirmation, and outgoing email.

   1. The pre-signup trigger validates the username, applies the new-user compute and model limits from global settings, and creates the user’s profile.

   1. The post-confirmation trigger adds the new user to the default racer group.

   1. The custom message trigger records a metric each time the user pool sends an email.

   1. When an administrator email is supplied at deployment, a custom resource creates that administrator and adds them to the admin group.

1.  [AWS WAF](https://aws.amazon.com/waf/) provides intelligent protection for the API against common attack vectors and allows customers to define custom rules based on individual use cases and usage patterns.

1.  [Amazon API Gateway](https://aws.amazon.com/api-gateway/) routes API requests to their appropriate handler using a defined Smithy model.

1. A single [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) table stores profiles, training jobs, models, evaluation jobs, submissions, leaderboards, events, tracks, runs, laps, rankings, fleets, devices, and deployments.

1. AWS Lambda API functions back the API, with one function per operation.

   1. Profiles, models, evaluations, leaderboards, and submissions: create, read, update, and delete operations, and sending training and evaluation jobs to the job queue. Creating or retrying a model first checks the account’s SageMaker training quotas. If either is full, the model waits for capacity and no job is queued until the user retries. Only training jobs wait this way; an evaluation that SageMaker rejects for capacity fails instead, because there is no status it could recover from.

   1. Model import and export: importing a virtual or physical model sends a job to the import queue. Retrieving a model’s asset URL starts the asset packaging function if no current package exists and reports the packaging as queued; a later call returns a pre-signed URL once the package is ready.

   1. Live races: facilitator queue management, including listing the queue, reordering submissions via fractional indexing, removing submissions, resetting in-progress or failed models, and clearing the leaderboard. Launching a race starts the live race workflow. Other functions declare a winner, and grant newly authenticated users the IoT Core policy they need to subscribe to race topics.

   1. Events: creating and editing events, their tracks and their fleets, moving an event through its statuses, recording runs and laps, and reading per-track and combined leaderboards. Deleting an event sends a cascade-delete request to the event delete queue.

   1. Devices: activating cars and timers through Systems Manager hybrid activation, listing, updating, and deleting them individually or in batches, and sending restart, stop, color change, and clear models commands to them.

   1. Model transfer: packaging a model for a physical car invokes the model optimizer, and deploying it to a car starts the push workflow.

   1. Users and settings: creating a Cognito user for a racer registered at an event, bulk user creation, and reading and updating global settings. Bulk user creation runs a separate [AWS Step Functions](https://aws.amazon.com/step-functions/) state machine that creates each submitted user and finalizes the batch once every entry has been processed.

1.  [AWS AppConfig](https://aws.amazon.com/systems-manager/features/appconfig/) hosted configuration stores application-level settings, such as usage quotas.

1. A user data bucket (Amazon S3) stores all user data including trained models, evaluation results, and other assets generated during the DeepRacer workflow.

1. An asset packaging AWS Lambda function packages a model’s assets from the user data bucket into the virtual model bucket for export. Packaging jobs that fail go to an [Amazon SQS](https://aws.amazon.com/sqs/) dead-letter queue.

1. A virtual model bucket (Amazon S3) stores exported models. The user’s browser downloads an exported model directly from this bucket using the pre-signed URL the API returns.

1. An Amazon SQS FIFO queue receives requests for training and evaluation jobs and stores them in FIFO order. A job that repeatedly fails to dispatch moves to a dead-letter queue rather than blocking the jobs behind it.

1. An AWS Step Functions training workflow runs each training or evaluation job from start to finish. If no training capacity is available, it cleans up and leaves the job waiting for capacity. Otherwise it polls the job every minute while it runs, and finalizes the job whether it succeeds or fails.

1. AWS Lambda workflow functions perform the steps of each job.

   1. The job dispatcher takes a job off the queue and starts the training workflow.

   1. The job initializer sets up the job, creates its video stream, and starts the SageMaker training job.

   1. The job monitor checks the status of the running job.

   1. The job finalizer records the result, collects the job’s logs, and cleans up its video stream.

   1. The live race workflow reuses the initializer, monitor, and finalizer to run race evaluations.

1.  [Amazon SageMaker](https://aws.amazon.com/sagemaker/) performs the actual training and evaluation of the model using the reward function and hyperparameters provided. Each job runs the DeepRacer training container image from Amazon ECR.

1.  [Amazon Kinesis Video Streams](https://aws.amazon.com/kinesis/video-streams/) carries the simulation video from the SageMaker job to the user’s browser.

1. An Amazon DynamoDB Stream captures item-level changes from the main table and delivers them to the race functions, enabling event-driven orchestration of live race evaluations and real-time broadcast of race state to spectators.

1. AWS Lambda race functions respond to live and physical race activity.

   1. The DynamoDB stream triggers the stream handler. It starts a live race workflow execution when one or more submissions with PENDING status exist in the queue, the race is IN\_PROGRESS, autolaunch is enabled, and no execution is currently running. It acquires the execution lock via a conditional write before starting the execution. Stream records it fails to process go to a dead-letter queue that raises an alarm.

   1. The DynamoDB stream also triggers the broadcast handler, which detects relevant state changes such as evaluation started or completed, leaderboard updates, and winner declarations. It publishes them to IoT Core, writes the public leaderboard JSON object, and emits a race-submitted event to the race event bus when a run finishes. When a device record expires through DynamoDB TTL, it fans the expired instance ids out to the device pruner. Records it fails to process go to a dead-letter queue that raises an alarm as soon as any message arrives.

   1. The SafetyNet function runs when a live race workflow execution reaches any terminal state. It clears the execution lock with a conditional write and applies a backoff check if the execution has failed repeatedly. It then touches a PENDING queue item to generate a DynamoDB stream event, which retriggers the stream handler if items remain in the queue.

   1. The stats rebuild function recalculates aggregate race statistics in response to a race-submitted event, and is limited to one concurrent execution so that rebuilds are serialized.

1. An AWS Step Functions live race workflow runs the queued submissions for a live race one at a time. The stream handler or a facilitator launching the race starts it. For each submission it runs the evaluation on SageMaker through the workflow functions, using four functions of its own:

   1. Get next pending takes the first pending queue item by position and loads its submission.

   1. Check autolaunch stops the loop when autolaunch is off or the race has completed.

   1. Update queue status moves the item through in progress, completed, and failed, with a conditional check so a facilitator reset is not overwritten.

   1. Clear execution lock releases the leaderboard’s lock as the last step, on both the success and the error path.

1.  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) routes race events.

   1. A custom event bus receives the race-submitted event from the broadcast handler and routes it to the stats rebuild function. Events that still fail once EventBridge has exhausted its retries go to a dead-letter queue, so a failed rebuild is retained for inspection rather than dropped.

   1. A rule on the live race workflow’s execution status changes invokes the SafetyNet function whenever an execution succeeds, fails, aborts, or times out.

1.  [AWS IoT Core](https://aws.amazon.com/iot-core/) provides a managed WebSocket pub/sub channel for delivering live race state updates to spectator and participant browsers. Each live race uses a dedicated Message Queuing Telemetry Transport (MQTT) topic scoped by leaderboard ID, physical race events use a per-event topic tree, and device status and command results go to the device management screens. Browsers subscribe via WebSocket, and the broadcast handler publishes via IAM-authorized HTTPS, so no connections table or custom connect and disconnect handlers are needed. Facilitator and administrator browsers also publish directly to IoT Core. They send race countdown, pause, and resume state and race topic updates without passing through Lambda, which keeps timing jitter low.

1. An Amazon SQS event delete queue receives a cascade-delete request when an event is deleted, so dependent records are removed asynchronously rather than inside the API request. Requests that keep failing go to a dead-letter queue for manual re-drive.

1. An event delete worker AWS Lambda function consumes the delete queue and removes the laps, runs, rankings, submissions, and tracks belonging to a deleted event, then the event record itself. It takes one message per invocation and is capped at two concurrent executions, so at most two events are torn down at a time.

1.  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) provides the hybrid activation that enrolls physical cars and timers as managed instances, and RunCommand for running commands on them. Systems Manager addresses each device by the managed instance id that hybrid activation assigned to it.

1. Physical devices (cars and timers) enroll themselves as managed instances using a hybrid activation code, and receive model deployments and control commands through Systems Manager. When a model is deployed, the car downloads it directly from the user data bucket using a pre-signed URL included in the command.

1. Amazon EventBridge device rules keep device status current.

   1. A rule captures Systems Manager instance association changes and command status changes, and invokes the state change handler.

   1. A schedule invokes the device status poller every five minutes.

1. AWS Lambda device functions track the state of each device.

   1. The state change handler records those changes against the matching device record, so the user interface reflects whether a car is online and how its last command finished.

   1. The device status poller reads managed instance information from Systems Manager and refreshes the stored status of each registered device.

   1. The device pruner deregisters the Systems Manager managed instance of each device whose record has expired through DynamoDB TTL.

1.  [Amazon GuardDuty](https://aws.amazon.com/guardduty/) malware protection scans physical models uploaded to the upload bucket and tags each object with the result. The model optimizer polls for that tag for up to a minute and proceeds only when the scan found no threats. A detected threat, an unscannable file, and a scan that failed or never reported all stop the import with a message instead. Malware scanning is on by default for any deployment built from the published template.

1. AWS Lambda model transfer functions prepare a model for a physical car and deliver it.

   1. The model optimizer, which runs from a container image in Amazon ECR, converts a trained or imported model into the format required by physical DeepRacer cars. Packaging a model invokes it asynchronously, and those requests go to a dead-letter queue when they fail, where a processor function marks the model’s optimization status as failed so that it does not stay stuck in progress. The import dispatcher invokes it synchronously instead, so a physical import that fails is retried by the import queue.

   1. The push functions send the transfer command to the car, poll for its completion, and update the deployment status for the push workflow.

1. An AWS Step Functions push workflow orchestrates transferring a model to a physical car. It marks the deployment in progress. It then sends the download and installation command to the car through Systems Manager RunCommand, along with a pre-signed URL for the model in the user data bucket. It polls until the command finishes and records the deployment as completed or failed.

1. An upload bucket (Amazon S3) stores uploaded (but not yet imported) assets from the user.

1. An Amazon SQS import queue receives import jobs from the API functions and holds them until they are accepted by the import dispatcher. Jobs that fail twice move to a dead-letter queue, where a handler marks the import as failed.

1. An AWS Step Functions import workflow validates an imported virtual model and brings it into the system. It validates the reward function, validates the model, imports the model assets, and records the import as complete, stopping at the first validation that fails.

1. AWS Lambda import functions perform the steps of each import.

   1. The import dispatcher takes a job off the import queue. For a virtual model, it starts the import workflow. For a physical model, it invokes the model optimizer directly.

   1. The reward function validator, which runs from a container image in Amazon ECR, checks and sanitizes the customer-provided reward function code before it is saved to the system. The same function validates reward functions when a model is created or tested.

   1. The model validator, which runs from a container image in Amazon ECR, checks the uploaded model.

   1. Both validators run in a VPC of private isolated subnets with no NAT gateway, behind a security group that allows no outbound traffic, so customer-provided code cannot reach the network.

   1. The import model assets function copies the model assets from the upload bucket into the user data bucket.

   1. The import completion handler records the final status of the import, whether it succeeded or failed validation.

   1. The failed request handler marks imports that reached the dead-letter queue as failed.

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
|  [Amazon EventBridge](https://aws.amazon.com/eventbridge/)  | Core | Routes race, live race workflow, and device events to their Lambda handlers, including the SafetyNet function. |
|  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)  | Core | Enrolls physical cars and timers as managed instances, and runs deployment and control commands on them. |
|  [AWS AppConfig](https://aws.amazon.com/systems-manager/features/appconfig/)  | Core | Stores application-level settings such as usage quotas. |
|  [AWS CodeBuild](https://aws.amazon.com/codebuild/)  | Core | Copies the container images the solution runs from public repositories into private Amazon ECR repositories at deployment. |
|  [Amazon Virtual Private Cloud (VPC)](https://aws.amazon.com/vpc/)  | Optional | Can be used to provide network isolation for SageMaker AI training jobs for enhanced security. |

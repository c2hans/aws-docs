---
source_url: https://docs.aws.amazon.com/solutions/physical-ai-production-designer-on-aws/index.html
---

---
title: 'Guidance for Physical AI Production Designer on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/physical-ai-production-designer-on-aws/
source: aws-documentation
generated_on: 2026-11-20
---

# Guidance for Physical AI Production Designer on AWS

## Overview

This Guidance helps manufacturers run the robot cell workflow, from product data to a commissioned cell, in one browser-based application on AWS. It connects the tools teams already use — product lifecycle management (PLM) systems and the engineering software and controllers from programmable logic controller (PLC) and robot vendors — rather than replacing them. Engineers import product data and state their intent; AI agents plan the cell and its robot motion, generate controller code or train a policy, and test the result in a virtual cell. After engineer and safety approval, factory sites pull the release, and live data closes the loop so the virtual cell runs the production code.

## Benefits

### Plan robot cells in hours, not weeks

State the product and process intent, and AI agents equip the robots with end-of-arm tooling, lay out the cell, assign tasks, and plan collision-free motion for multiple robots. Engineers review and approve each plan in 3D in the browser. This replaces weeks of manual cell planning, repeated for every product variant, with agent-driven iterations on AWS.

### Generate control code and AI policies

Turn approved plans into deterministic IEC 61131-3 programmable logic controller (PLC) programs and native robot programs that run on the controllers already on your shop floor. Where a cell must handle a variety of products, train an AI policy that drives the robots in real time.

### Catch faults before the floor

Test generated code and trained policies in disposable virtual cells, where virtual PLCs and virtual robot controllers run alongside NVIDIA Isaac Sim physics simulation, all connected in one closed loop. Inject faults in tests that run the same code or policy that ships to the cell. You surface collisions, cycle-time misses, and logic errors in simulation instead of on costly production hardware.

## How it works

This architecture diagram illustrates how to build and operate Physical AI Production Designer on AWS. It shows the key components and their interactions. [Download the architecture diagram](downloads/physical-ai-production-designer.pdf)

### AWS architecture

Step 1Engineers state product intent, chat with AI agents, and review 3D cells in the Physical AI (PAI) Production Designer viewer. Amazon CloudFront serves this WebAssembly app over HTTPS. Engineers sign in with single sign-on (SSO): Amazon Cognito federates over TLS with your OpenID Connect (OIDC) identity provider; Lambda@Edge authorizes requests.

Step 2An Elastic Load Balancing (ELB) Application Load Balancer inside your Amazon Virtual Private Cloud (Amazon VPC) routes engineers to workspaces. On Amazon Elastic Kubernetes Service (Amazon EKS), Kiro agents drive Model Context Protocol (MCP) tools. Amazon Bedrock AgentCore securely deploys and operates agents of any framework or model at scale.

Step 3Planners use fully managed Amazon Bedrock foundation models with security, privacy, and responsible AI. Agents test generated programmable logic controller (PLC) and robot code in virtual cells. Amazon Elastic Compute Cloud (Amazon EC2) runs Isaac Sim; Amazon DCV streams vendor tools. Amazon SageMaker AI builds and trains machine learning policies.

Step 4Import product lifecycle management (PLM) data into Amazon Simple Storage Service (Amazon S3) over TLS. It encrypts data at rest and invokes AWS Lambda to log changes. Amazon Elastic Container Registry (Amazon ECR) stores container images. Workloads get settings from AWS Systems Manager and scoped credentials from AWS Secrets Manager.

Step 5AWS Step Functions gates the release: G0 virtual commissioning; engineers approve G1, safety engineers G2. AWS Signer signs it; AWS IoT Greengrass deploys it. Perimeter network edge hosts authenticate, pull it outbound-only over TLS, and check G3. Amazon EKS Anywhere runs cell controllers; operators confirm G4, and drift flows back.

### Experience and orchestration

Step 6In the PAI Production Designer viewer, engineers review cells in 3D and use tool pages, terminals, agent chat, and behaviour-tree timelines. Amazon CloudFront, a content delivery network (CDN), serves the WebAssembly (WASM) app. Lambda@Edge authenticates single sign-on (SSO) requests; Amazon Cognito federates your OpenID Connect (OIDC) identity provider.

Step 7CloudFront carries three TLS streams: HTTPS, Zenoh, and Amazon DCV for human-machine interfaces (HMIs). An Application Load Balancer from Elastic Load Balancing in your Amazon Virtual Private Cloud (Amazon VPC) routes them to user workspaces. Each least-privilege Linux container on Amazon Elastic Kubernetes Service (Amazon EKS) hosts a backend API.

Step 8Engineers and the Kiro agent drive modules over Model Context Protocol (MCP), and plan2cell generates programmable logic controller (PLC) and robot programs. The planner router calls the multi robot agentic solver, a large language model (LLM) planner. Fully managed Amazon Bedrock provides foundation models with security, privacy, and responsible AI.

Step 9Zenoh, a low-latency peer-to-peer data plane, links the viewer, workspaces, virtual cells, and Isaac Sim with publish/subscribe and queries. It carries scene deltas, joint states at controller rate, PLC signals, behaviour-tree events, controller commands, and live controller data. Viewer, agents, and cells share one live state.

Step 10Amazon Bedrock AgentCore keeps agent memory and securely deploys and operates agents of any framework or model at scale. Amazon Simple Storage Service (Amazon S3) hosts viewer builds and stores product lifecycle management (PLM) bills of materials (BOMs) and specs, encrypted at rest. AWS Lambda logs catalogue changes.

### Virtual cells and simulation

Step 11Every engineer and agent gets a disposable virtual cell from Git. A Zenoh mesh links it to your user workspace, which deploys generated robot and programmable logic controller (PLC) code. Closed-loop tests inject faults. Failures return to the agent; engineers get passing code as a pull request with test evidence.

Step 12Cells run on Amazon Elastic Kubernetes Service (Amazon EKS) nodes. The cell runtime runs policy inference and steers virtual robot controllers. PROFINET or another fieldbus carries cyclic I/O to sensors, the HMI, and an International Electrotechnical Commission (IEC) 61131-3 virtual PLC. Generated code runs unchanged, as on the shop floor.

Step 13PLC and robot vendor integrated development environments (IDEs) run on a Windows Amazon Elastic Compute Cloud (Amazon EC2) host. Amazon DCV streams them over TLS for online debugging in the viewer. NVIDIA Isaac Sim on a graphics processing unit (GPU) host reruns the code; its physics can contradict the plan.

Step 14Fully managed Amazon SageMaker AI builds, trains, and evaluates machine learning policies for the cell runtime. Least-privilege containers pull images from Amazon Elastic Container Registry (Amazon ECR), settings from AWS Systems Manager, and credentials from AWS Secrets Manager. Amazon Simple Storage Service (Amazon S3) encrypts backups at rest.

### On-premises deployment

Step 15Engineers upload programmable logic controller (PLC) and robot projects to versioned Amazon Simple Storage Service (Amazon S3) buckets. Uploads start releases in AWS Step Functions, the single gatekeeper. AWS CodeBuild builds code, images, and software bills of materials. At G0, virtual controllers run unchanged code, checking cycle times and collisions.

Step 16Humans gate the boundary, not the sandbox. Controls or robot engineers approve G1; for safety changes, a safety engineer and change board approve G2 through Step Functions task tokens. AWS Signer signs bundles with approval attestations. Amazon S3 Object Lock and Amazon Elastic Container Registry (Amazon ECR) store them encrypted.

Step 17AWS IoT Greengrass rolls releases out in waves. AWS IoT Core runs jobs; Amazon DynamoDB and Amazon S3 Object Lock store approvals, simulation evidence, and device status. The edge host in the plant perimeter network, an International Electrotechnical Commission (IEC) 62443 zone, pulls deployments over TLS; the cloud never pushes.

Step 18The release agent verifies signatures and attestations and checks G3: a maintenance window, safe cell, backup, and no active manufacturing execution system (MES) order. It deploys head PLC, cell controller, and HMI containers to Amazon EKS Anywhere; the Windows edge host loads the safety PLC and robot controllers.

Step 19In the cell network, a fieldbus links PLCs, robots, and the HMI. Only adapters cross one restricted conduit into it. Each adapter backs up, checks drift, deploys, reads back, verifies, and reports; rollback restores its backup.

Step 20At G4, the operator confirms a reduced-speed cycle on the teach pendant; motion never starts remotely. The Zenoh bridge streams drift over TLS to the PAI Production Designer twin on Amazon Elastic Kubernetes Service (Amazon EKS). Operational technology (OT) asset management keeps device versions.

### User workspace

Step 21Engineers chat with the AI agent and approve cells in 3D in the Physical AI (PAI) Production Designer viewer. Lambda@Edge on Amazon CloudFront checks the OpenID Connect (OIDC) login. An Application Load Balancer from Elastic Load Balancing (ELB) terminates HTTPS for least-privilege containers on Amazon Elastic Kubernetes Service (Amazon EKS).

Step 22The backend, the only entry point, proxies Zenoh, desktop, WebRTC, and teach-pendant sessions. Cell tools deploy programmable logic controller (PLC) and robot code and solve inverse kinematics (IK). The Kiro agent uses its Kiro service chat model, speaks Agent Client Protocol (ACP), and drives modules through Model Context Protocol (MCP).

Step 23The MCP planner router starts planner jobs that compare robot counts, placements, and task orders. Burst jobs add Amazon Elastic Compute Cloud (Amazon EC2) instances. The multi robot agentic solver, a large language model (LLM) planner, invokes foundation models on Amazon Bedrock, a fully managed service with security and privacy.

Step 24The live bridge reads the head PLC over OPC UA and virtual robot controllers over Zenoh, read-only, and publishes the live scene. A proxy relays Amazon DCV from the Windows integrated development environment (IDE) host. Cell tools deploy through its PLC IDE MCP bridge with an AWS Secrets Manager token.

Step 25The Isaac bridge links NVIDIA Isaac Sim on graphics processing unit (GPU) hosts to Zenoh, outbound over secure WebSocket. Workspaces install the release named in Parameter Store in AWS Systems Manager. Amazon Simple Storage Service (Amazon S3) holds releases, user data, and backups, encrypted at rest. AWS Lambda controls cells.

## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-physical-ai-production-designer-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)

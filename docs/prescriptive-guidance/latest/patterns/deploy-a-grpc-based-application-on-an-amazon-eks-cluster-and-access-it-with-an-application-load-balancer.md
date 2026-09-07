---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-a-grpc-based-application-on-an-amazon-eks-cluster-and-access-it-with-an-application-load-balancer.html
---

# Deploy a gRPC-based application on an Amazon EKS cluster and access it with an Application Load Balancer
<a name="deploy-a-grpc-based-application-on-an-amazon-eks-cluster-and-access-it-with-an-application-load-balancer"></a>

*Kirankumar Chandrashekar and Huy Nguyen, Amazon Web Services*

## Summary
<a name="deploy-a-grpc-based-application-on-an-amazon-eks-cluster-and-access-it-with-an-application-load-balancer-summary"></a>

This pattern describes how to host a gRPC-based application on an Amazon Elastic Kubernetes Service (Amazon EKS) cluster and securely access it through an Application Load Balancer.

[gRPC](https://grpc.io/) is an open-source remote procedure call (RPC) framework that can run in any environment. You can use it for microservice integrations and client-server communications. For more information about gRPC, see the AWS blog post [Application Load Balancer support for end-to-end HTTP/2 and gRPC](https://aws.amazon.com/blogs/aws/new-application-load-balancer-support-for-end-to-end-http-2-and-grpc/).

This pattern shows you how to host a gRPC-based application that runs on Kubernetes pods on Amazon EKS. The gRPC client connects to an Application Load Balancer through the HTTP/2 protocol with an SSL/TLS encrypted connection. The Application Load Balancer forwards traffic to the gRPC application that runs on Amazon EKS pods. The number of gRPC pods can be automatically scaled based on traffic by using the [Kubernetes Horizontal Pod Autoscaler](https://docs.aws.amazon.com/eks/latest/userguide/horizontal-pod-autoscaler.html). The Application Load Balancer's target group performs health checks on the Amazon EKS nodes, evaluates if the target is healthy, and forwards traffic only to healthy nodes.

## Prerequisites and limitations
<a name="deploy-a-grpc-based-application-on-an-amazon-eks-cluster-and-access-it-with-an-application-load-balancer-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ [Docker](https://www.docker.com/), installed and configured on Linux, macOS, or Windows.
+ [AWS Command Line Interface (AWS CLI) version 2](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html), installed and configured on Linux, macOS, or Windows.
+ [eksctl](https://github.com/eksctl-io/eksctl#installation), installed and configured on Linux, macOS, or Windows.
+ `kubectl`, installed and configured to access resources on your Amazon EKS cluster. For more information, see [Installing or updating kubectl](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html) in the Amazon EKS documentation.
+ [gRPCurl](https://github.com/fullstorydev/grpcurl), installed and configured.
+ A new or existing Amazon EKS cluster. For more information, see [Getting started with Amazon EKS.](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html)
+ Your computer terminal configured to access the Amazon EKS cluster. For more information, see [Configure your computer to communicate with your cluster](https://docs.aws.amazon.com/eks/latest/userguide/getting-started-console.html#eks-configure-kubectl) in the Amazon EKS documentation.
+ [AWS Load Balancer Controller](https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html), provisioned in the Amazon EKS cluster.
+ An existing DNS host name with a valid SSL or SSL/TLS certificate. You can obtain a certificate for your domain by using AWS Certificate Manager (ACM) or uploading an existing certificate to ACM. For more information about these two options, see [Requesting a public certificate](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html) and [Importing certificates into AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the ACM documentation.

## Architecture
<a name="deploy-a-grpc-based-application-on-an-amazon-eks-cluster-and-access-it-with-an-application-load-balancer-architecture"></a>

The following diagram shows the architecture implemented by this pattern.

![Architecture for gRPC-based application on Amazon EKS](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/abf727c1-ff8b-43a7-923f-bce825d1b459/images/281936fa-bc43-4b4e-a343-ba1eab97df38.png)

The following diagram shows a workflow where SSL/TLS traffic is received from a gRPC client that offloads to an Application Load Balancer. Traffic is forwarded in plaintext to the gRPC server because it comes from a virtual private cloud (VPC).

![Workflow for sending SSL/TLS traffic to a gRPC server](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/abf727c1-ff8b-43a7-923f-bce825d1b459/images/09e0c3f6-0c39-40b7-908f-8c4c693a5f02.png)

## Tools
<a name="deploy-a-grpc-based-application-on-an-amazon-eks-cluster-and-access-it-with-an-application-load-balancer-tools"></a>

**AWS services**
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command line shell.
+ [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) distributes incoming application or network traffic across multiple targets. For example, you can distribute traffic across Amazon Elastic Compute Cloud (Amazon EC2) instances, containers, and IP addresses in one or more Availability Zones.
+ [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) is a managed container image registry service that’s secure, scalable, and reliable.
+ [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) helps you run Kubernetes on AWS without needing to install or maintain your own Kubernetes control plane or nodes.

**Tools**
+ [eksctl](https://eksctl.io/) is a simple CLI tool for creating clusters on Amazon EKS.
+ [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) is a command line utility for running commands against Kubernetes clusters.
+ [AWS Load Balancer Controller](https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html) helps you manage AWS Elastic Load Balancers for a Kubernetes cluster.
+ [gRPCurl ](https://github.com/fullstorydev/grpcurl)is a command line tool that helps you interact with gRPC services.

**Code repository**

The code for this pattern is available in the GitHub [grpc-traffic-on-alb-to-eks](https://github.com/aws-samples/grpc-traffic-on-alb-to-eks.git) repository.

## Epics
<a name="deploy-a-grpc-based-application-on-an-amazon-eks-cluster-and-access-it-with-an-application-load-balancer-epics"></a>

### Build and push the gRPC server’s Docker image to Amazon ECR
<a name="build-and-push-the-grpc-serverrsquor-s-docker-image-to-amazon-ecr"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Amazon ECR repository. | Sign in to the AWS Management Console, open the [Amazon ECR console](https://console.aws.amazon.com/ecr/), and then create an Amazon ECR repository. For more information, see [Creating a repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html) in the Amazon ECR documentation. Make sure that you record the Amazon ECR repository’s URL.<br />You can also create an Amazon ECR repository with AWS CLI by running the following command:<pre>aws ecr create-repository --repository-name helloworld-grpc</pre> | Cloud administrator |
| Build the Docker image.  | 1. Clone the GitHub [grpc-traffic-on-alb-to-eks](https://github.com/aws-samples/grpc-traffic-on-alb-to-eks.git) repository.<pre>git clone https://github.com/aws-samples/grpc-traffic-on-alb-to-eks.git</pre><br />2. From the root directory of the repository, make sure that the Dockerfile exists and then run the following command to build the Docker image: <pre>docker build -t <amazon_ecr_repository_url>:<Tag> .</pre>Make sure that you replace `<amazon_ecr_repository_url>`  with the URL of the Amazon ECR repository that you created earlier. | DevOps engineer |
| Push the Docker image to Amazon ECR. | 1. Run the following command to log in to the Amazon ECR repository:<pre>aws ecr get-login-password --region us-east-1 --no-cli-auto-prompt | docker login --username AWS --password-stdin <your_aws_account_id>.dkr.ecr.us-east-1.amazonaws.com</pre><br />2. Push the Docker image to the Amazon ECR repository by running the following command:<pre>docker push <your_aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/helloworld-grpc:1.0</pre>Make sure that you replace `<your_aws_account_id>`  with your AWS account ID. | DevOps engineer |

### Deploy the Kubernetes manifests to the Amazon EKS cluster
<a name="deploy-the-kubernetes-manifests-to-the-amazon-eks-cluster"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Modify the values in the Kubernetes manifest file. | 1. Modify the `grpc-sample.yaml` Kubernetes manifest file in the Kubernetes folder of the repository according to your requirements. You must modify the annotations and host name in the ingress resource. For a sample ingress resource, see the [Additional information](#deploy-a-grpc-based-application-on-an-amazon-eks-cluster-and-access-it-with-an-application-load-balancer-additional) section. For more information about ingress annotations, see [Ingress annotations](https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.4/guide/ingress/annotations/) in the Kubernetes documentation.<br />2. In the Kubernetes deployment resource, change the deployment resource's `image` to the uniform resource identifier (URI) for the Amazon ECR repository that you pushed the Docker image to. For a sample deployment resource, see the [Additional information](#deploy-a-grpc-based-application-on-an-amazon-eks-cluster-and-access-it-with-an-application-load-balancer-additional) section. | DevOps engineer |
| Deploy the Kubernetes manifest file.  | Deploy the `grpc-sample.yaml` file to the Amazon EKS cluster by running the following `kubectl` command: <pre>kubectl apply -f ./kubernetes/grpc-sample.yaml</pre> | DevOps engineer |

### Create the DNS record for the Application Load Balancer's FQDN
<a name="create-the-dns-record-for-the-application-load-balancerapos-s-fqdn"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Record the FQDN for the Application Load Balancer. | 1. Run the following `kubectl` command to describe the Kubernetes ingress resource that manages the Application Load Balancer:<pre>kubectl get ingress -n grpcserver</pre><br />Sample output is provided in the [Additional information](#deploy-a-grpc-based-application-on-an-amazon-eks-cluster-and-access-it-with-an-application-load-balancer-additional) section. In the output, the `HOSTS` field displays the DNS host name that the SSL certificates were created for.<br />2. Record the Application Load Balancer’s fully qualified domain name (FQDN) from the `Address` field of the output. <br />3. Create a DNS record that points to the Application Load Balancer's FQDN. If your DNS provider is Amazon Route 53, you can create an alias record that points to the Application Load Balancer's FQDN. For more information about this option, see [Choosing between alias and non-alias records](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html) in the Route 53 documentation. | DevOps engineer |

### Test the solution
<a name="test-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Test the gRPC server.  | Use gRPCurl to test the endpoint by running the following command:<pre>grpcurl grpc.example.com:443 list <br />grpc.reflection.v1alpha.ServerReflection<br />helloworld.helloworld</pre>Replace `grpc.example.com` with your DNS name. | DevOps engineer |
| Test the gRPC server using a gRPC client.  | In the `helloworld_client_ssl.py` sample gRPC client, replace the host name from `grpc.example.com` with the host name used for the gRPC server.  <br />The following code sample shows the response from the gRPC server for the client's request:<pre>python ./app/helloworld_client_ssl.py<br />message: "Hello to gRPC server from Client"<br /><br />message: "Thanks for talking to gRPC server!! Welcome to hello world. Received message is \"Hello to gRPC server from Client\""<br />received: true</pre><br />This shows that the client can talk to the server and that the connection is successful. | DevOps engineer |

### Clean up
<a name="clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Remove the DNS record. | Remove the DNS record that points to the Application Load Balancer's FQDN that you created earlier.  | Cloud administrator |
| Remove the load balancer. | On the [Amazon EC2 console](https://console.aws.amazon.com/ec2/), choose **Load Balancers**, and then remove the load balancer that the Kubernetes controller created for your ingress resource. | Cloud administrator |
| Delete the Amazon EKS cluster. | Delete the Amazon EKS cluster by using `eksctl`:<pre>eksctl delete cluster -f ./eks.yaml</pre> | AWS DevOps |

## Related resources
<a name="deploy-a-grpc-based-application-on-an-amazon-eks-cluster-and-access-it-with-an-application-load-balancer-resources"></a>
+ [Network load balancing on Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/load-balancing.html)
+ [Target groups for your Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html#target-group-protocol-version)

## Additional information
<a name="deploy-a-grpc-based-application-on-an-amazon-eks-cluster-and-access-it-with-an-application-load-balancer-additional"></a>

**Sample ingress resource:**

```
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    alb.ingress.kubernetes.io/healthcheck-protocol: HTTP
    alb.ingress.kubernetes.io/ssl-redirect: "443"
    alb.ingress.kubernetes.io/backend-protocol-version: "GRPC"
    alb.ingress.kubernetes.io/listen-ports: '[{"HTTP": 80}, {"HTTPS":443}]'
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/target-type: ip
    alb.ingress.kubernetes.io/certificate-arn: arn:aws:acm:<AWS-Region>:<AccountId>:certificate/<certificate_ID>
  labels:
    app: grpcserver
    environment: dev
  name: grpcserver
  namespace: grpcserver
spec:
  ingressClassName: alb
  rules:
  - host: grpc.example.com # <----- replace this as per your host name for which the SSL certtficate is available in ACM
    http:
      paths:
      - backend:
          service:
            name: grpcserver
            port:
              number: 9000
        path: /
        pathType: Prefix
```

**Sample deployment resource:**

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: grpcserver
  namespace: grpcserver
spec:
  selector:
    matchLabels:
      app: grpcserver
  replicas: 1
  template:
    metadata:
      labels:
        app: grpcserver
    spec:
      containers:
      - name: grpc-demo
        image: <your_aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/helloworld-grpc:1.0   #<------- Change to the URI that the Docker image is pushed to
        imagePullPolicy: Always
        ports:
        - name: grpc-api
          containerPort: 9000
        env:
        - name: POD_IP
          valueFrom:
            fieldRef:
              fieldPath: status.podIP
      restartPolicy: Always
```

**Sample output:**

```
NAME             CLASS           HOSTS                          Address                PORTS          AGE
 grpcserver      <none>      <DNS-HostName>                  <ELB-address>              80            27d
```

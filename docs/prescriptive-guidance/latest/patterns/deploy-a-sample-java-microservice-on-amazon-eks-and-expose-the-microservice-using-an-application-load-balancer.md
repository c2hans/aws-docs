---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-a-sample-java-microservice-on-amazon-eks-and-expose-the-microservice-using-an-application-load-balancer.html
---

# Deploy a sample Java microservice on Amazon EKS and expose the microservice using an Application Load Balancer
<a name="deploy-a-sample-java-microservice-on-amazon-eks-and-expose-the-microservice-using-an-application-load-balancer"></a>

*Vijay Thompson and Akkamahadevi Hiremath, Amazon Web Services*

## Summary
<a name="deploy-a-sample-java-microservice-on-amazon-eks-and-expose-the-microservice-using-an-application-load-balancer-summary"></a>

This pattern describes how to deploy a sample Java microservice as a containerized application on Amazon Elastic Kubernetes Service (Amazon EKS) by using the `eksctl` command line utility and Amazon Elastic Container Registry (Amazon ECR). You can use an Application Load Balancer to load balance the application traffic.

## Prerequisites and limitations
<a name="deploy-a-sample-java-microservice-on-amazon-eks-and-expose-the-microservice-using-an-application-load-balancer-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ The AWS Command Line Interface (AWS CLI) version 1.7 or later, installed and configured on macOS, Linux, or Windows
+ A running [Docker daemon](https://docs.docker.com/config/daemon/)
+ The `eksctl` command line utility, installed and configured on macOS, Linux, or Windows (For more information, see [Getting started with Amazon EKS – eksctl](https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html) in the Amazon EKS documentation.)
+ The `kubectl` command line utility, installed and configured on macOS, Linux, or Windows (For more information, see [Installing or updating kubectl](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html) in the Amazon EKS documentation.)

**Limitations**
+ This pattern doesn’t cover the installation of an SSL certificate for the Application Load Balancer.

## Architecture
<a name="deploy-a-sample-java-microservice-on-amazon-eks-and-expose-the-microservice-using-an-application-load-balancer-architecture"></a>

**Target technology stack**
+ Amazon ECR
+ Amazon EKS
+ Elastic Load Balancing

**Target architecture**

The following diagram shows an architecture for containerizing a Java microservice on Amazon EKS.

![A Java microservice deployed as a containerized application on Amazon EKS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e1dd8ab0-9e1e-4d2b-b7af-89d3e583e57c/images/aaca4fd9-5aaa-4df5-aebd-02a2ed881c3b.png)

## Tools
<a name="deploy-a-sample-java-microservice-on-amazon-eks-and-expose-the-microservice-using-an-application-load-balancer-tools"></a>
+ [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) is a managed container image registry service that’s secure, scalable, and reliable.
+ [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) helps you run Kubernetes on AWS without needing to install or maintain your own Kubernetes control plane or nodes.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell.
+ [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) automatically distributes your incoming traffic across multiple targets, such as Amazon Elastic Compute Cloud (Amazon EC2) instances, containers, and IP addresses, in one or more Availability Zones.
+ [eksctl](https://eksctl.io/) helps you create clusters on Amazon EKS.
+ [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) makes it possible to run commands against Kubernetes clusters.
+ [Docker](https://www.docker.com/) helps you build, test, and deliver applications in packages called containers.

## Epics
<a name="deploy-a-sample-java-microservice-on-amazon-eks-and-expose-the-microservice-using-an-application-load-balancer-epics"></a>

### Create an Amazon EKS cluster by using eksctl
<a name="create-an-amazon-eks-cluster-by-using-eksctl"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Amazon EKS cluster.  | To create an Amazon EKS cluster that uses two t2.small Amazon EC2 instances as nodes, run the following command:<pre>eksctl create cluster --name <your-cluster-name> --version <version-number> --nodes=1 --node-type=t2.small</pre>The process can take between 15 to 20 minutes. After the cluster is created, the appropriate Kubernetes configuration is added to your [kubeconfig](https://docs.aws.amazon.com/eks/latest/userguide/create-kubeconfig.html) file. You can use the `kubeconfig` file with `kubectl`** **to deploy the application in later steps. | Developer, System Admin |
| Verify the Amazon EKS cluster. | To verify that the cluster is created and that you can connect to it, run the `kubectl get nodes` command. | Developer, System Admin |

### Create an Amazon ECR repository and push the Docker image.
<a name="create-an-amazon-ecr-repository-and-push-the-docker-image"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Amazon ECR repository. | Follow the instructions from [Creating a private repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html) in the Amazon ECR documentation. | Developer, System Admin |
| Create a POM XML file. | Create a `pom.xml` file based on the *Example POM file *code in the [Additional information](#deploy-a-sample-java-microservice-on-amazon-eks-and-expose-the-microservice-using-an-application-load-balancer-additional) section of this pattern. | Developer, System Admin |
| Create a source file. | Create a source file called `HelloWorld.java` in the `src/main/java/eksExample` path based on the following example:<pre>package eksExample;<br />import static spark.Spark.get;<br /><br />public class HelloWorld {<br />    public static void main(String[] args) {<br />        get("/", (req, res) -> {<br />            return "Hello World!";<br />        });<br />    }<br />}</pre><br />Be sure to use the following directory structure:<pre>├── Dockerfile<br />├── deployment.yaml<br />├── ingress.yaml<br />├── pom.xml<br />├── service.yaml<br />└── src<br />    └── main<br />        └── java<br />            └── eksExample<br />                └── HelloWorld.java</pre> |  |
| Create a Dockerfile. | Create a `Dockerfile` based on the *Example Dockerfile *code in the [Additional information](#deploy-a-sample-java-microservice-on-amazon-eks-and-expose-the-microservice-using-an-application-load-balancer-additional) section of this pattern. | Developer, System Admin |
| Build and push the Docker image. | In the directory where you want your `Dockerfile` to build, tag, and push the image to Amazon ECR, run the following commands:<pre>aws ecr get-login-password --region <region>| docker login --username <username> --password-stdin <account_number>.dkr.ecr.<region>.amazonaws.com<br />docker buildx build --platform linux/amd64 -t hello-world-java:v1 .<br />docker tag hello-world-java:v1 <account_number>.dkr.ecr.<region>.amazonaws.com/<repository_name>:v1<br />docker push <account_number>.dkr.ecr.<region>.amazonaws.com/<repository_name>:v1</pre>Modify the AWS Region, account number, and repository details in the preceding commands. Be sure to note the image URL for later use.A macOS system with an M1 chip has a problem building an image that’s compatible with Amazon EKS running on an AMD64 platform. To resolve this issue, use [docker buildx](https://docs.docker.com/engine/reference/commandline/buildx/) to build a Docker image that works on Amazon EKS. |  |

### Deploy the Java microservices
<a name="deploy-the-java-microservices"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a deployment file.  | Create a YAML file called `deployment.yaml` based on the *Example deployment file *code in the [Additional information](#deploy-a-sample-java-microservice-on-amazon-eks-and-expose-the-microservice-using-an-application-load-balancer-additional) section of this pattern.Use the image URL that you copied earlier as the path of the image file for the Amazon ECR repository. | Developer, System Admin |
| Deploy the Java microservices on the Amazon EKS cluster.  | To create a deployment in your Amazon EKS cluster, run the `kubectl apply -f deployment.yaml` command. | Developer, System Admin |
| Verify the status of the pods. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-a-sample-java-microservice-on-amazon-eks-and-expose-the-microservice-using-an-application-load-balancer.html) | Developer, System Admin |
| Create a service. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-a-sample-java-microservice-on-amazon-eks-and-expose-the-microservice-using-an-application-load-balancer.html) | Developer, System Admin |
| Install the AWS Load Balancer Controller add-on. | Follow the instructions from [Installing the AWS Load Balancer Controller add-on](https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html) in the Amazon EKS documentation.You must have the add-on installed to create an Application Load Balancer or Network Load Balancer for a Kubernetes service. | Devloper, System Admin |
| Create an ingress resource. | Create a YAML file called `ingress.yaml` based on the *Example ingress resource file *code in the [Additional information](#deploy-a-sample-java-microservice-on-amazon-eks-and-expose-the-microservice-using-an-application-load-balancer-additional) section of this pattern. | Developer, System Admin |
| Create an Application Load Balancer. | To deploy the ingress resource and create an Application Load Balancer, run the `kubectl apply -f ingress.yaml` command. | Developer, System Admin |

### Test the application
<a name="test-the-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Test and verify the application. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-a-sample-java-microservice-on-amazon-eks-and-expose-the-microservice-using-an-application-load-balancer.html) | Developer, System Admin |

## Related resources
<a name="deploy-a-sample-java-microservice-on-amazon-eks-and-expose-the-microservice-using-an-application-load-balancer-resources"></a>
+ [Creating a private repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html) (Amazon ECR documentation)
+ [Pushing a Docker image](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html) (Amazon ECR documentation)
+ [Ingress Controllers](https://www.eksworkshop.com/beginner/130_exposing-service/ingress_controller_alb/) (Amazon EKS Workshop)
+ [Docker buildx](https://docs.docker.com/engine/reference/commandline/buildx/) (Docker docs)

## Additional information
<a name="deploy-a-sample-java-microservice-on-amazon-eks-and-expose-the-microservice-using-an-application-load-balancer-additional"></a>

**Example POM file**

```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>helloWorld</groupId>
  <artifactId>helloWorld</artifactId>
  <version>1.0-SNAPSHOT</version>

  <dependencies>
    <dependency>
      <groupId>com.sparkjava</groupId><artifactId>spark-core</artifactId><version>2.0.0</version>
    </dependency>
  </dependencies>
  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId><artifactId>maven-jar-plugin</artifactId><version>2.4</version>
        <configuration><finalName>eksExample</finalName><archive><manifest>
              <addClasspath>true</addClasspath><mainClass>eksExample.HelloWorld</mainClass><classpathPrefix>dependency-jars/</classpathPrefix>
            </manifest></archive>
        </configuration>
      </plugin>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId><artifactId>maven-compiler-plugin</artifactId><version>3.1</version>
        <configuration><source>1.8</source><target>1.8</target></configuration>
      </plugin>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId><artifactId>maven-assembly-plugin</artifactId>
        <executions>
          <execution>
            <goals><goal>attached</goal></goals><phase>package</phase>
            <configuration>
              <finalName>eksExample</finalName>
              <descriptorRefs><descriptorRef>jar-with-dependencies</descriptorRef></descriptorRefs>
              <archive><manifest><mainClass>eksExample.HelloWorld</mainClass></manifest></archive>
            </configuration>
          </execution>
        </executions>
      </plugin>
    </plugins>
  </build>
</project>
```

**Example Dockerfile**

```
FROM bellsoft/liberica-openjdk-alpine-musl:17

RUN apk add maven
WORKDIR /code

# Prepare by downloading dependencies
ADD pom.xml /code/pom.xml
RUN ["mvn", "dependency:resolve"]
RUN ["mvn", "verify"]

# Adding source, compile and package into a fat jar
ADD src /code/src
RUN ["mvn", "package"]

EXPOSE 4567
CMD ["java", "-jar", "target/eksExample-jar-with-dependencies.jar"]
```

**Example deployment file**

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: microservice-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app.kubernetes.io/name: java-microservice
  template:
    metadata:
      labels:
        app.kubernetes.io/name: java-microservice
    spec:
      containers:
      - name: java-microservice-container
        image: .dkr.ecr.amazonaws.com/:
        ports:
        - containerPort: 4567
```

**Example service file**

```
apiVersion: v1
kind: Service
metadata:
  name: "service-java-microservice"
spec:
  ports:
    - port: 80
      targetPort: 4567
      protocol: TCP
  type: NodePort
  selector:
    app.kubernetes.io/name: java-microservice
```

**Example ingress resource file**

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: "java-microservice-ingress"
  annotations:
    kubernetes.io/ingress.class: alb
    alb.ingress.kubernetes.io/load-balancer-name: apg2
    alb.ingress.kubernetes.io/target-type: ip
  labels:
    app: java-microservice
spec:
  rules:
    - http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: "service-java-microservice"
                port:
                  number: 80
```

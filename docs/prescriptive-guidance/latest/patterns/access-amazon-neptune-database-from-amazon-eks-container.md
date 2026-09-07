---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-amazon-neptune-database-from-amazon-eks-container.html
---

# Access an Amazon Neptune database from an Amazon EKS container
<a name="access-amazon-neptune-database-from-amazon-eks-container"></a>

*Ramakrishnan Palaninathan, Amazon Web Services*

## Summary
<a name="access-amazon-neptune-database-from-amazon-eks-container-summary"></a>

This pattern establishes a connection between Amazon Neptune, which is a fully managed graph database, and Amazon Elastic Kubernetes Service (Amazon EKS), a container orchestration service, to access a Neptune database. Neptune DB clusters are confined within a virtual private cloud (VPC) on AWS. For this reason, accessing Neptune requires careful configuration of the VPC to enable connectivity.

Unlike Amazon Relational Database Service (Amazon RDS) for PostgreSQL, Neptune doesn't rely on typical database access credentials. Instead, it uses AWS Identity and Access Management (IAM) roles for authentication. Therefore, connecting to Neptune from Amazon EKS involves setting up an IAM role with the necessary permissions to access Neptune.

Furthermore, Neptune endpoints are accessible only within the VPC where the cluster resides. This means that you have to configure network settings to facilitate communication between Amazon EKS and Neptune. Depending on your specific requirements and networking preferences, there are [various approaches to configuring the VPC](https://docs.aws.amazon.com/neptune/latest/userguide/get-started-vpc.html) to enable seamless connectivity between Neptune and Amazon EKS. Each method offers distinct advantages and considerations, which provide flexibility in designing your database architecture to suit your application's needs.

## Prerequisites and limitations
<a name="access-amazon-neptune-database-from-amazon-eks-container-prereqs"></a>

**Prerequisites **
+ Install the latest version of **kubectl** (see [instructions](https://kubernetes.io/docs/tasks/tools/#kubectl)). To check your version, run:

  ```
  kubectl version --short
  ```
+ Install the latest version of **eksctl** (see [instructions](https://eksctl.io/installation/)). To check your version, run:

  ```
  eksctl info
  ```
+ Install the latest version of the AWS Command Line Interface (AWS CLI) version 2 (see [instructions](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)). To check your version, run:

  ```
  aws --version
  ```
+ Create a Neptune DB cluster (see [instructions](https://docs.aws.amazon.com/neptune/latest/userguide/get-started-cfn-create.html)). Make sure to establish communications between the cluster's VPC and Amazon EKS through [VPC peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html), [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-getting-started.html), or another method. Also make sure that the status of the cluster is "available" and that it has an inbound rule on port 8182 for the security group.
+ Configure an IAM OpenID Connect (OIDC) provider on an existing Amazon EKS cluster (see [instructions](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html)).

**Product versions**
+ [Amazon EKS 1.27](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html)
+ [Amazon Neptune engine version 1.3.0.0 (2023-11-15)](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases-1.3.0.0.html)

## Architecture
<a name="access-amazon-neptune-database-from-amazon-eks-container-architecture"></a>

The following diagram shows the connection between Kubernetes pods in an Amazon EKS cluster and Neptune to provide access to a Neptune database.

![Connecting pods in a Kubernetes node with Amazon Neptune.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/2fcf9e00-1664-462a-825e-b0fdd962f478/images/86da67e5-340e-4b29-acc6-2da416ce57eb.png)

**Automation and scale**

You can use the Amazon EKS [Horizontal Pod Autoscaler ](https://docs.aws.amazon.com/eks/latest/userguide/horizontal-pod-autoscaler.html)to scale this solution.

## Tools
<a name="access-amazon-neptune-database-from-amazon-eks-container-tools"></a>

**Services**
+ [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) helps you run Kubernetes on AWS without needing to install or maintain your own Kubernetes control plane or nodes.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [Amazon Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/intro.html) is a graph database service that helps you build and run applications that work with highly connected datasets.

## Best practices
<a name="access-amazon-neptune-database-from-amazon-eks-container-best-practices"></a>

For best practices, see [Identity and Access Management](https://aws.github.io/aws-eks-best-practices/security/docs/iam/) in the *Amazon EKS Best Practices Guides*.

## Epics
<a name="access-amazon-neptune-database-from-amazon-eks-container-epics"></a>

### Set environment variables
<a name="set-environment-variables"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Verify the cluster context. | Before you interact with your Amazon EKS cluster by using Helm or other command-line tools, you must define environment variables that encapsulate your cluster's details. These variables are used in subsequent commands to ensure that they target the correct cluster and resources.<br />First, confirm that you are operating within the correct cluster context. This ensures that any subsequent commands are sent to the intended Kubernetes cluster. To verify the current context, run the following command.<pre>kubectl config current-context</pre> | AWS administrator, Cloud administrator |
| Define the `CLUSTER_NAME` variable. | Define the `CLUSTER_NAME` environment variable for your Amazon EKS cluster. In the following command, replace the sample value `us-west-2` with the correct AWS Region for your cluster. Replace the sample value `eks-workshop` with your existing cluster name.<pre>export CLUSTER_NAME=$(aws eks describe-cluster --region us-west-2 --name eks-workshop --query "cluster.name" --output text)</pre> | AWS administrator, Cloud administrator |
| Validate output. | To validate that the variables have been set properly, run the following command.<pre>echo $CLUSTER_NAME</pre><br />Verify that the output of this command matches the input you specified in the previous step. | AWS administrator, Cloud administrator |

### Create IAM role and associate it with Kubernetes
<a name="create-iam-role-and-associate-it-with-kubernetes"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a service account. | You use [IAM roles for service accounts](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html?sc_channel=el&sc_campaign=appswave&sc_content=eks-integrate-secrets-manager&sc_geo=mult&sc_country=mult&sc_outcome=acq) to map your Kubernetes service accounts to IAM roles, to enable fine-grained permissions management for your applications that run on Amazon EKS. You can use [eksctl](https://eksctl.io/) to create and associate an IAM role with a specific Kubernetes service account within your Amazon EKS cluster. The AWS managed policy `NeptuneFullAccess` allows write and read access to your specified Neptune cluster.You must have an [OIDC endpoint](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html?sc_channel=el&sc_campaign=appswave&sc_content=eks-integrate-secrets-manager&sc_geo=mult&sc_country=mult&sc_outcome=acq) associated with your cluster before you run these commands.<br />Create a service account that you want to associate with an AWS managed policy named `NeptuneFullAccess`.<pre>eksctl create iamserviceaccount --name eks-neptune-sa --namespace default --cluster $CLUSTER_NAME --attach-policy-arn arn:aws:iam::aws:policy/NeptuneFullAccess --approve --override-existing-serviceaccounts</pre><br />where `eks-neptune-sa `is the name of the service account that you want to create.<br />Upon completion, this command displays the following response:<pre>2024-02-07 01:12:39 [ℹ] created serviceaccount "default/eks-neptune-sa"</pre> | AWS administrator, Cloud administrator |
| Verify that the account is set up properly. | Make sure that the `eks-neptune-sa` service account is set up correctly in the default namespace in your cluster.<pre>kubectl get sa eks-neptune-sa -o yaml</pre><br />The output should look like this:<pre>apiVersion: v1<br />kind: ServiceAccount<br />metadata:<br />  annotations:<br />    eks.amazonaws.com/role-arn: arn:aws:iam::123456789123:role/eksctl-eks-workshop-addon-iamserviceaccount-d-Role1-Q35yKgdQOlmM<br />  creationTimestamp: "2024-02-07T01:12:39Z"<br />  labels:<br />    app.kubernetes.io/managed-by: eksctl<br />  name: eks-neptune-sa<br />  namespace: default<br />  resourceVersion: "5174750"<br />  uid: cd6ba2f7-a0f5-40e1-a6f4-4081e0042316</pre> | AWS administrator, Cloud administrator |
| Check connectivity. | Deploy a sample pod called `pod-util` and check connectivity with Neptune.<pre>apiVersion: v1<br />kind: Pod<br />metadata:<br />  name: pod-util<br />  namespace: default<br />spec:<br />  serviceAccountName: eks-neptune-sa<br />  containers:<br />  - name: pod-util<br />    image: public.ecr.aws/patrickc/troubleshoot-util<br />    command:<br />      - sleep<br />      - "3600"<br />    imagePullPolicy: IfNotPresent</pre><pre>kubectl apply -f pod-util.yaml</pre><pre>kubectl exec --stdin --tty pod-util -- /bin/bash<br />bash-5.1# curl -X POST -d '{"gremlin":"g.V().limit(1)"}' https://db-neptune-1.cluster-xxxxxxxxxxxx.us-west-2.neptune.amazonaws.com:8182/gremlin<br />{"requestId":"a4964f2d-12b1-4ed3-8a14-eff511431a0e","status":{"message":"","code":200,"attributes":{"@type":"g:Map","@value":[]}},"result":{"data":{"@type":"g:List","@value":[]},"meta":{"@type":"g:Map","@value":[]}}}<br />bash-5.1# exit<br />exit</pre> | AWS administrator, Cloud administrator |

### Validate connection activity
<a name="validate-connection-activity"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Enable IAM database authentication. | By default, IAM database authentication is disabled when you create a Neptune DB cluster. You can enable or disable IAM database authentication by using the AWS Management Console.<br />Follow the steps in the AWS documentation to [enable IAM database authentication in Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth-enable.html). | AWS administrator, Cloud administrator |
| Verify connections. | In this step, you interact with the `pod-util` container, which is already in running status, to install **awscurl **and verify the connection.1. Run the following command to find the pod.<pre>kubectl get pods</pre><br />The output should look like this:<pre>NAME READY STATUS RESTARTS AGE<br />pod-util 1/1 Running 0 50m</pre><br />2. Run the following command to install **awscurl**.<pre>kubectl exec --stdin --tty pod-util -- /bin/bash bash-5.1#pip3 install awscurl Installing collected packages: idna, configparser, configargparse, charset-normalizer, certifi, requests, awscurl Successfully installed awscurl-0.32 certifi-2024.2.2 charset-normalizer-3.3.2 configargparse-1.7 configparser-6.0.0 idna-3.6 requests-2.31.0 bash-5.1# awscurl https://db-neptune-1.cluster-xxxxxxxxxxxx.us-west-2.neptune.amazonaws.com:8182/status --region us-west-2 --service neptune-db {"status":"healthy","startTime":"Thu Feb 08 01:22:14 UTC 2024","dbEngineVersion":"1.3.0.0.R1","role":"writer","dfeQueryEngine":"viaQueryHint","gremlin":{"version":"tinkerpop-3.6.4"},"sparql":{"version":"sparql-1.1"},"opencypher":{"version":"Neptune-9.0.20190305-1.0"},"labMode":{"ObjectIndex":"disabled","ReadWriteConflictDetection":"enabled"},"features":{"SlowQueryLogs":"disabled","ResultCache":{"status":"disabled"},"IAMAuthentication":"enabled","Streams":"disabled","AuditLog":"disabled"},"settings":{"clusterQueryTimeoutInMs":"120000","SlowQueryLogsThreshold":"5000"}}</pre> | AWS administrator, Cloud administrator |

## Troubleshooting
<a name="access-amazon-neptune-database-from-amazon-eks-container-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Can't access the Neptune database. | Review the IAM policy that's attached to the service account. Make sure that it allows the necessary actions (for example, `neptune:Connec,neptune:DescribeDBInstances`) for the operations you want to run. |

## Related resources
<a name="access-amazon-neptune-database-from-amazon-eks-container-resources"></a>
+ [Grant Kubernetes workloads access to AWS using Kubernetes Service Accounts](https://docs.aws.amazon.com/eks/latest/userguide/service-accounts.html) (Amazon EKS documentation)
+ [IAM roles for service accounts](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) (Amazon EKS documentation)
+ [Creating a new Neptune DB cluster](https://docs.aws.amazon.com/neptune/latest/userguide/get-started-create-cluster.html) (Amazon Neptune documentation)

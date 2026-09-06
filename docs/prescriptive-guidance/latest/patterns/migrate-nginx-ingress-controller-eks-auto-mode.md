---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-nginx-ingress-controller-eks-auto-mode.html
---

# Migrate NGINX Ingress Controllers when enabling Amazon EKS Auto Mode
<a name="migrate-nginx-ingress-controller-eks-auto-mode"></a>

*Olawale Olaleye and Shamanth Devagari, Amazon Web Services*

## Summary
<a name="migrate-nginx-ingress-controller-eks-auto-mode-summary"></a>

[EKS Auto Mode](https://docs.aws.amazon.com/eks/latest/userguide/automode.html) for Amazon Elastic Kubernetes Service (Amazon EKS) can reduce the operational overhead of running your workloads on Kubernetes clusters. This mode allows AWS to also set up and manage the infrastructure on your behalf. When you enable EKS Auto Mode on an existing cluster, you must carefully plan the migration of [NGINX Ingress Controller](https://docs.nginx.com/nginx-ingress-controller/overview/about/) configurations. This is because the direct transfer of Network Load Balancers isn't possible.

You can use a blue/green deployment strategy to migrate an NGINX Ingress Controller instance when you enable EKS Auto Mode in an existing Amazon EKS cluster.

## Prerequisites and limitations
<a name="migrate-nginx-ingress-controller-eks-auto-mode-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An [Amazon EKS cluster](https://docs.aws.amazon.com/eks/latest/userguide/create-cluster.html) running Kubernetes version 1.29 or later
+ Amazon EKS add-ons running [minimum versions](https://docs.aws.amazon.com/eks/latest/userguide/auto-enable-existing.html#auto-addons-required)
+ Latest version of [kubectl](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html#kubectl-install-update)
+ An existing [NGINX Ingress Controller](https://kubernetes.github.io/ingress-nginx/deploy/#aws) instance
+ (Optional) A [hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-working-with.html) in Amazon Route 53 for DNS-based traffic shifting

## Architecture
<a name="migrate-nginx-ingress-controller-eks-auto-mode-architecture"></a>

A *blue/green deployment* is a deployment strategy in which you create two separate but identical environments. Blue/green deployments provide near-zero downtime release and rollback capabilities. The fundamental idea is to shift traffic between two identical environments that are running different versions of your application.

The following image shows the migration of Network Load Balancers from two different NGINX Ingress Controller instances when enabling EKS Auto Mode. You use a blue/green deployment to shift traffic between the two Network Load Balancers.

![Using a blue/green deployment strategy to migrate NGINX Ingress Controller instances.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/57e8c14f-cb50-4027-8ef6-ce8ea3f2db25/images/211a029a-90d8-4c92-8200-19e54062f936.png)

The original namespace is the *blue* namespace. This is where the original NGINX Ingress Controller service and instance run, before you enable EKS Auto Mode. The original service and instance connect to a Network Load Balancer that has a DNS name that is configured in Route 53. The [AWS Load Balancer Controller](https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.11/) deployed this Network Load Balancer in the target virtual private cloud (VPC).

The diagram shows the following workflow to set up an environment for a blue/green deployment:

1. Install and configure another NGINX Ingress Controller instance in a different namespace, a *green* namespace.

1. In Route 53, configure a DNS name for a new Network Load Balancer.

## Tools
<a name="migrate-nginx-ingress-controller-eks-auto-mode-tools"></a>

**AWS services**
+ [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) helps you run Kubernetes on AWS without needing to install or maintain your own Kubernetes control plane or nodes.
+ [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) distributes incoming application or network traffic across multiple targets. For example, you can distribute traffic across Amazon Elastic Compute Cloud (Amazon EC2) instances, containers, and IP addresses in one or more Availability Zones.
+ [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) is a highly available and scalable DNS web service.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

**Other tools**
+ [Helm](https://helm.sh/) is an open source package manager for Kubernetes that helps you install and manage applications on your Kubernetes cluster.
+ [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) is a command-line interface that helps you run commands against Kubernetes clusters.
+ [NGINX Ingress Controller](https://docs.nginx.com/nginx-ingress-controller/overview/about/) connects Kubernetes apps and services with request handling, auth, self-service custom resources, and debugging.

## Epics
<a name="migrate-nginx-ingress-controller-eks-auto-mode-epics"></a>

### Review the existing environment
<a name="review-the-existing-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Confirm that the original NGINX Ingress Controller instance is operational. | Enter the following command to verify that the resources in the `ingress-nginx` namespace are operational. If you have deployed NGINX Ingress Controller in another namespace, update the namespace name in this command.<pre>kubectl get all -n ingress-nginx</pre><br />In the output, confirm that NGINX Ingress Controller pods are in running state. The following is an example output:<pre>NAME                                           READY   STATUS      RESTARTS      AGE<br />pod/ingress-nginx-admission-create-xqn9d       0/1     Completed   0             88m<br />pod/ingress-nginx-admission-patch-lhk4j        0/1     Completed   1             88m<br />pod/ingress-nginx-controller-68f68f859-xrz74   1/1     Running     2 (10m ago)   72m<br /><br />NAME                                         TYPE           CLUSTER-IP       EXTERNAL-IP                                                                     PORT(S)                      AGE<br />service/ingress-nginx-controller             LoadBalancer   10.100.67.255    k8s-ingressn-ingressn-abcdefg-12345.elb.eu-west-1.amazonaws.com   80:30330/TCP,443:31462/TCP   88m<br />service/ingress-nginx-controller-admission   ClusterIP      10.100.201.176   <none>                                                                          443/TCP                      88m<br /><br />NAME                                       READY   UP-TO-DATE   AVAILABLE   AGE<br />deployment.apps/ingress-nginx-controller   1/1     1            1           88m<br /><br />NAME                                                 DESIRED   CURRENT   READY   AGE<br />replicaset.apps/ingress-nginx-controller-68f68f859   1         1         1       72m<br />replicaset.apps/ingress-nginx-controller-d8c96cf68   0         0         0       88m<br /><br />NAME                                       STATUS     COMPLETIONS   DURATION   AGE<br />job.batch/ingress-nginx-admission-create   Complete   1/1           4s         88m<br />job.batch/ingress-nginx-admission-patch    Complete   1/1           5s         88m</pre> | DevOps engineer |

### Deploy a sample HTTPd workload to use the NGINX Ingress Controller
<a name="deploy-a-sample-httpd-workload-to-use-the-nginx-ingress-controller"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Kubernetes resources. | Enter the following commands to create a sample Kubernetes deployment, service, and ingress:<pre>kubectl create deployment demo --image=httpd --port=80</pre><pre>kubectl expose deployment demo</pre><pre> kubectl create ingress demo --class=nginx \<br />  --rule nginxautomode.local.dev/=demo:80</pre> | DevOps engineer |
| Review the deployed resources. | Enter the following command to view a list of the deployed resources:<pre>kubectl get all,ingress</pre><br />In the output, confirm that the sample HTTPd pod is in a running state. The following is an example output:<pre>NAME                        READY   STATUS    RESTARTS   AGE<br />pod/demo-7d94f8cb4f-q68wc   1/1     Running   0          59m<br /><br />NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE<br />service/demo         ClusterIP   10.100.78.155   <none>        80/TCP    59m<br />service/kubernetes   ClusterIP   10.100.0.1      <none>        443/TCP   117m<br /><br />NAME                   READY   UP-TO-DATE   AVAILABLE   AGE<br />deployment.apps/demo   1/1     1            1           59m<br /><br />NAME                              DESIRED   CURRENT   READY   AGE<br />replicaset.apps/demo-7d94f8cb4f   1         1         1       59m<br /><br />NAME                             CLASS   HOSTS                                  ADDRESS                                                                         PORTS   AGE<br />ingress.networking.k8s.io/demo   nginx   nginxautomode.local.dev                k8s-ingressn-ingressn-abcdefg-12345.elb.eu-west-1.amazonaws.com                 80      56m</pre> | DevOps engineer |
| Confirm the service is reachable. | Enter the following command to confirm that the service is reachable through the DNS name of the Network Load Balancer:<pre>curl -H "Host: nginxautomode.local.dev" http://k8s-ingressn-ingressn-abcdefg-12345.elb.eu-west-1.amazonaws.com</pre><br />The following is the expected output:<pre><html><body><h1>It works!</h1></body></html></pre> | DevOps engineer |
| (Optional) Create a DNS record. | 1. Follow the instructions in [Creating records by using the Amazon Route 53 console](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html) (Route 53 documentation) to create a DNS record for the configured domain.<br />2. Enter the following command to confirm that the service is reachable through the configured domain name:<pre>curl "http://nginxautomode.local.dev/?[1-5]"</pre><br />The following is the expected output:<pre><html><body><h1>It works!</h1></body></html><br /><html><body><h1>It works!</h1></body></html><br /><html><body><h1>It works!</h1></body></html><br /><html><body><h1>It works!</h1></body></html><br /><html><body><h1>It works!</h1></body></html></pre> | DevOps engineer, AWS DevOps |

### Enable EKS Auto Mode on the existing cluster
<a name="enable-eks-auto-mode-on-the-existing-cluster"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Enable EKS Auto Mode. | Follow the instructions in [Enable EKS Auto Mode on an existing cluster](https://docs.aws.amazon.com/eks/latest/userguide/auto-enable-existing.html) (Amazon EKS documentation). | AWS DevOps |

### Install a new NGINX Ingress Controller
<a name="install-a-new-nginx-ingress-controller"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure a new NGINX Ingress Controller instance. | 1. Download the [deploy.yaml](https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.12.0/deploy/static/provider/aws/deploy.yaml) template.<br />2. Open the **deploy.yaml** template in your preferred editor.<br />3. In the `kind: Namespace` section, enter a unique name for the namespace, such as `ingress-nginx-v2`:<pre>apiVersion: v1<br />kind: Namespace<br />metadata:<br />  labels:<br />    app.kubernetes.io/instance: ingress-nginx<br />    app.kubernetes.io/name: ingress-nginx<br />  name: ingress-nginx-v2</pre><br />4. For each section, update the `namespace` value to the new name.<br />5. In the `kind: Deployment` section, do the following:Enter a unique value for `--controller-class`, such as `k8s.io/ingress-nginx-v2`.Enter a unique value for `--ingress-class`, such as `nginx-v2`.<pre>apiVersion: apps/v1<br />kind: Deployment<br />  name: ingress-nginx-controller<br />  namespace: ingress-nginx-v2<br />...  <br />    spec:<br />      containers:<br />      - args:<br />        - /nginx-ingress-controller<br />        - --publish-service=$(POD_NAMESPACE)/ingress-nginx-controller<br />        - --election-id=ingress-nginx-leader<br />        - --controller-class=k8s.io/ingress-nginx-v2<br />        - --ingress-class=nginx-v2</pre><br />6. In the `kind: IngressClass` section, enter the same values for `--controller-class` and `--ingress-class` that you used in the previous section:<pre>apiVersion: networking.k8s.io/v1<br />kind: IngressClass<br />metadata:<br />  labels:<br />    app.kubernetes.io/component: controller<br />    app.kubernetes.io/instance: ingress-nginx<br />    app.kubernetes.io/name: ingress-nginx<br />    app.kubernetes.io/part-of: ingress-nginx<br />    app.kubernetes.io/version: 1.12.0<br />  name: nginx-v2<br />spec:<br />  controller: k8s.io/ingress-nginx-v2</pre><br />7. In the following section, add `loadBalancerClass: eks.amazonaws.com/nlb` to provision a Network Load Balancer for the NGINX Ingress Controller instance:<pre>apiVersion: v1<br />kind: Service<br />metadata:<br />  name: ingress-nginx-controller<br />  namespace: ingress-nginx-v2<br />spec:<br />...<br />  selector:<br />    app.kubernetes.io/component: controller<br />    app.kubernetes.io/instance: ingress-nginx<br />    app.kubernetes.io/name: ingress-nginx<br />  type: LoadBalancer<br />  loadBalancerClass: eks.amazonaws.com/nlb</pre><br />8. Save and close the **deploy.yaml** template. | DevOps engineer |
| Deploy the new NGINX Instance Controller instance. | Enter the following command to apply the modified manifest file:<pre>kubectl apply -f deploy.yaml</pre> | DevOps engineer |
| Confirm successful deployment. | Enter the following command to verify that the resources in the `ingress-nginx-v2` namespace are operational:<pre>kubectl get all -n ingress-nginx-v2</pre><br />In the output, confirm that NGINX Ingress Controller pods are in a running state. The following is an example output:<pre>NAME                                            READY   STATUS      RESTARTS   AGE<br />pod/ingress-nginx-admission-create-7shrj        0/1     Completed   0          24s<br />pod/ingress-nginx-admission-patch-vkxr5         0/1     Completed   1          24s<br />pod/ingress-nginx-controller-757bfcbc6d-4fw52   1/1     Running     0          24s<br /><br />NAME                                         TYPE           CLUSTER-IP       EXTERNAL-IP                                                                     PORT(S)                      AGE<br />service/ingress-nginx-controller             LoadBalancer   10.100.208.114   k8s-ingressn-ingressn-2e5e37fab6-848337cd9c9d520f.elb.eu-west-1.amazonaws.com   80:31469/TCP,443:30658/TCP   24s<br />service/ingress-nginx-controller-admission   ClusterIP      10.100.150.114   <none>                                                                          443/TCP                      24s<br /><br />NAME                                       READY   UP-TO-DATE   AVAILABLE   AGE<br />deployment.apps/ingress-nginx-controller   1/1     1            1           24s<br /><br />NAME                                                  DESIRED   CURRENT   READY   AGE<br />replicaset.apps/ingress-nginx-controller-757bfcbc6d   1         1         1       24s<br /><br />NAME                                       STATUS     COMPLETIONS   DURATION   AGE<br />job.batch/ingress-nginx-admission-create   Complete   1/1           4s         24s<br />job.batch/ingress-nginx-admission-patch    Complete   1/1           5s         24s</pre> | DevOps engineer |
| Create a new ingress for the sample HTTPd workload. | Enter the following command to create a new ingress for the existing sample HTTPd workload:<pre>kubectl create ingress demo-new --class=nginx-v2 \<br />  --rule nginxautomode.local.dev/=demo:80</pre> | DevOps engineer |
| Confirm that the new ingress works. | Enter the following command to confirm that the new ingress works:<pre>curl -H "Host: nginxautomode.local.dev" k8s-ingressn-ingressn-2e5e37fab6-848337cd9c9d520f.elb.eu-west-1.amazonaws.com</pre><br />The following is the expected output:<pre><html><body><h1>It works!</h1></body></html></pre> | DevOps engineer |

### Cut over
<a name="cut-over"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Cut over to the new namespace. | 1. (Optional) Follow the instructions in [Editing records](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-editing.html) (Route 53 documentation) to update the DNS record.<br />2. When you have confirmed that the new NGINX Ingress Controller instance is operating as expected, delete the original.<br />3. Delete the self-managed AWS Load Balancer Controller. For instructions, see [Migrate apps from deprecated ALB Ingress Controller](https://docs.aws.amazon.com/eks/latest/userguide/lbc-remove.html) (Amazon EKS documentation).<br />4. Drain the managed node groups. For instructions, see [Deleting and draining node groups](https://eksctl.io/usage/nodegroups/#deleting-and-draining-nodegroups) (eksctl documentation). | AWS DevOps, DevOps engineer |
| Review the two ingresses. | Enter the following command to review the two ingresses that were created for the sample HTTPd workload:<pre>kubectl get ingress</pre><br />The following is an example output:<pre>NAME       CLASS      HOSTS                                  ADDRESS                                                                         PORTS   AGE<br />demo       nginx      nginxautomode.local.dev   k8s-ingressn-ingressn-abcdefg-12345.elb.eu-west-1.amazonaws.com                              80      95m<br />demo-new   nginx-v2   nginxautomode.local.dev   k8s-ingressn-ingressn-2e5e37fab6-848337cd9c9d520f.elb.eu-west-1.amazonaws.com                80      33s</pre> | DevOps engineer |

## Related resources
<a name="migrate-nginx-ingress-controller-eks-auto-mode-resources"></a>
+ [Enable EKS Auto Mode on an existing cluster](https://docs.aws.amazon.com/eks/latest/userguide/auto-enable-existing.html) (Amazon EKS documentation)
+ [Troubleshoot load balancers created by the Kubernetes service controller in Amazon EKS](https://repost.aws/knowledge-center/eks-load-balancers-troubleshooting) (AWS re:Post Knowledge Center)
+ [NGINX Ingress Controller](https://docs.nginx.com/nginx-ingress-controller/) (NGINX documentation)

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-mutual-tls-authentication-for-applications-running-on-amazon-eks.html
---

# Configure mutual TLS authentication for applications running on Amazon EKS
<a name="configure-mutual-tls-authentication-for-applications-running-on-amazon-eks"></a>

*Mahendra Revanasiddappa, Amazon Web Services*

## Summary
<a name="configure-mutual-tls-authentication-for-applications-running-on-amazon-eks-summary"></a>

Certificate-based mutual Transport Layer Security (TLS) is an optional TLS component that provides two-way peer authentication between servers and clients. With mutual TLS, clients must provide an X.509 certificate during the session negotiation process. The server uses this certificate to identify and authenticate the client.

Mutual TLS is a common requirement for Internet of Things (IoT) applications and can be used for business-to-business applications or standards such as [Open Banking](https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/open-banking.html).

This pattern describes how to configure mutual TLS for applications running on an Amazon Elastic Kubernetes Service (Amazon EKS) cluster by using an NGINX ingress controller. You can enable built-in mutual TLS features for the NGINX ingress controller by annotating the ingress resource. For more information about mutual TLS annotations on NGINX controllers, see [Client certificate authentication](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/#client-certificate-authentication) in the Kubernetes documentation.

**Important**
This pattern uses self-signed certificates. We recommend that you use this pattern only with test clusters, and not in production environments. If you want to use this pattern in a production environment, you can use [AWS Private Certificate Authority (AWS Private CA)](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html) or your existing public key infrastructure (PKI) standard to issue private certificates.

## Prerequisites and limitations
<a name="configure-mutual-tls-authentication-for-applications-running-on-amazon-eks-prereqs"></a>

**Prerequisites **
+ An active Amazon Web Services (AWS) account.
+ An existing Amazon EKS cluster.
+ AWS Command Line Interface (AWS CLI) version 1.7 or later, installed and configured on macOS, Linux, or Windows.
+ The kubectl command line utility, installed and configured to access the Amazon EKS cluster. For more information about this, see [Installing kubectl](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html) in the Amazon EKS documentation.
+ An existing Domain Name System (DNS) name to test the application.

**Limitations **
+ This pattern uses self-signed certificates. We recommend that you use this pattern only with test clusters, and not in production environments.

## Architecture
<a name="configure-mutual-tls-authentication-for-applications-running-on-amazon-eks-architecture"></a>

![Configuring mutual TLS authentication for applications running on Amazon EKS](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/ae2761e3-7ed2-4c2a-ba54-a4ddce8a1e7e/images/cefc60f9-2f29-4052-b7ae-df4eb6395e1c.png)

**Technology stack**
+ Amazon EKS
+ Amazon Route 53
+ Kubectl

## Tools
<a name="configure-mutual-tls-authentication-for-applications-running-on-amazon-eks-tools"></a>
+ [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) helps you run Kubernetes on AWS without needing to install or maintain your own Kubernetes control plane or nodes.
+ [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) is a highly available and scalable DNS web service.
+ [Kubectl](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html) is a command line utility that you use to interact with an Amazon EKS cluster.

## Epics
<a name="configure-mutual-tls-authentication-for-applications-running-on-amazon-eks-epics"></a>

### Generate the self-signed certificates
<a name="generate-the-self-signed-certificates"></a>

| Task | Description | Skills required |
| --- | --- | --- |
|  Generate the CA key and certificate. | Generate the certificate authority (CA) key and certificate by running the following command.<pre>openssl req -x509 -sha256 -newkey rsa:4096 -keyout ca.key -out ca.crt -days 356 -nodes -subj '/CN=Test Cert Authority'</pre> | DevOps engineer |
| Generate the server key and certificate, and sign with the CA certificate. | Generate the server key and certificate, and sign with the CA certificate by running the following command.<pre>openssl req -new -newkey rsa:4096 -keyout server.key -out server.csr -nodes -subj '/CN= <your_domain_name> ' && openssl x509 -req -sha256 -days 365 -in server.csr -CA ca.crt -CAkey ca.key -set_serial 01 -out server.crt</pre>Make sure sure that you replace `<your_domain_name>` with your existing domain name. | DevOps engineer |
|  Generate the client key and certificate, and sign with the CA certificate. | Generate the client key and certificate, and sign with the CA certificate by running the following command.<pre>openssl req -new -newkey rsa:4096 -keyout client.key -out client.csr -nodes -subj '/CN=Test' && openssl x509 -req -sha256 -days 365 -in client.csr -CA ca.crt -CAkey ca.key -set_serial 02 -out client.crt</pre> | DevOps engineer |

### Deploy the NGINX ingress controller
<a name="deploy-the-nginx-ingress-controller"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the NGINX ingress controller in your Amazon EKS cluster. | Deploy the NGINX ingress controller by using the following command.<pre>kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.7.0/deploy/static/provider/aws/deploy.yaml</pre> | DevOps engineer |
|  Verify that the NGINX ingress controller service is running. | Verify that the NGINX ingress controller service is running by using the following command.<pre>kubectl get svc -n ingress-nginx</pre>Make sure that the field of service address contains the Network Load Balancer’s domain name. | DevOps engineer |

### Create a namespace in the Amazon EKS cluster to test mutual TLS
<a name="create-a-namespace-in-the-amazon-eks-cluster-to-test-mutual-tls"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a namespace in the Amazon EKS cluster.  | Create a namespace called `mtls` in your Amazon EKS cluster by running the following command. <pre>kubectl create ns mtls</pre><br />This deploys the sample application to test mutual TLS. | DevOps engineer |

### Create the deployment and service for the sample application
<a name="create-the-deployment-and-service-for-the-sample-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Kubernetes deployment and service in the mtls namespace. | Create a file named `mtls.yaml`. Paste the following code into the file. <pre>kind: Deployment<br />apiVersion: apps/v1<br />metadata:<br />  name: mtls-app<br />  labels:<br />    app: mtls<br />spec:<br />  replicas: 1<br />  selector:<br />    matchLabels:<br />      app: mtls<br />  template:<br />    metadata:<br />      labels:<br />        app: mtls<br />    spec:<br />      containers:<br />      - name: mtls-app<br />        image: hashicorp/http-echo<br />        args:<br />          - "-text=mTLS is working"<br /><br /><br />---<br /><br />kind: Service<br />apiVersion: v1<br />metadata:<br />  name: mtls-service<br />spec:<br />  selector:<br />    app: mtls<br />  ports:<br />    - port: 5678 # Default port for image</pre><br /> Create the Kubernetes deployment and service in the `mtls` namespace by running the following command.<pre>kubectl create -f mtls.yaml -n mtls</pre> | DevOps engineer |
| Verify that the Kubernetes deployment is created. | Run the following command to verify that the deployment is created and has one pod in available status.<pre>kubectl get deploy -n mtls</pre> | DevOps engineer |
| Verify that the Kubernetes service is created. | Verify that the Kubernetes service is created by running the following command.<pre>kubectl get service -n mtls</pre> | DevOps engineer |

### Create a secret in the mtls namespace
<a name="create-a-secret-in-the-mtls-namespace"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a secret for the ingress resource. | Run the folllowing command to create a secret for the NGINX ingress controller by using the certificates that you created earlier.<pre>kubectl create secret generic mtls-certs --from-file=tls.crt=server.crt --from-file=tls.key=server.key --from-file=ca.crt=ca.crt -n mtls </pre><br />Your secret has a server certificate for the client to identify the server and a CA certificate for the server to verify the client certificates. | DevOps engineer |

### Create the ingress resource in the mtls namespace
<a name="create-the-ingress-resource-in-the-mtls-namespace"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the ingress resource in the mtls namespace. | Create a file named `ingress.yaml`. Paste the following code into the file (replace `<your_domain_name>` with your existing domain name).<pre>apiVersion: networking.k8s.io/v1<br />kind: Ingress<br />metadata:<br />  annotations:<br />    nginx.ingress.kubernetes.io/auth-tls-verify-client: "on"<br />    nginx.ingress.kubernetes.io/auth-tls-secret: mtls/mtls-certs<br />  name: mtls-ingress<br />spec:<br />  ingressClassName: nginx<br />  rules:<br />  - host: "*.<your_domain_name>"<br />    http:<br />      paths:<br />      - path: /<br />        pathType: Prefix<br />        backend:<br />          service:<br />            name: mtls-service<br />            port:<br />              number: 5678<br />  tls:<br />  - hosts:<br />    - "*.<your_domain_name>"<br />    secretName: mtls-certs</pre><br />Create the ingress resource in the `mtls` namespace  by running the following command.<pre>kubectl create -f ingress.yaml -n mtls</pre><br />This means that the NGINX ingress controller can route traffic to your sample application. | DevOps engineer |
| Verify that the ingress resource is created. | Verify that the ingress resource is created by running the following command.<pre>kubectl get ing -n mtls</pre>Make sure that the address of the ingress resource shows the load balancer created for the NGINX ingress controller. | DevOps engineer |

### Configure DNS to point the hostname to the load balancer
<a name="configure-dns-to-point-the-hostname-to-the-load-balancer"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create CNAME record that points to the load balancer for the NGINX ingress controller. | Sign in to the AWS Management Console, open the Amazon Route 53 console, and create a Canonical Name (CNAME) record that points `mtls.<your_domain_name>` to the load balancer for the NGINX ingress controller.<br />For more information, see [Creating records by using the Route 53 console](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html) in the Route 53 documentation. | DevOps engineer |

### Test the application
<a name="test-the-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Test mutual TLS setup without certificates. | Run the following command.<pre>curl -k https://mtls.<your_domain_name> </pre><br />You should receive the "400 No required SSL certificate was sent" error response. | DevOps engineer |
| Test mutual TLS setup with certificates. | Run the following command.<pre>curl -k https://mtls.<your_domain_name> --cert client.crt --key client.key</pre><br />You should receive the "mTLS is working" response. | DevOps engineer |

## Related resources
<a name="configure-mutual-tls-authentication-for-applications-running-on-amazon-eks-resources"></a>
+ [Creating records by using the Amazon Route 53 console](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html)
+ [Using a Network Load Balancer with the NGINX ingress controller on Amazon EKS](https://aws.amazon.com/blogs/opensource/network-load-balancer-nginx-ingress-controller-eks/)
+ [Client Certificate Authentication](https://kubernetes.github.io/ingress-nginx/examples/auth/client-certs/)

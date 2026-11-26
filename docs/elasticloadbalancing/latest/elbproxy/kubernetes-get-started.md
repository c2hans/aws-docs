---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/kubernetes-get-started.html
---

# Getting started

This walkthrough installs the controller, then deploys a sample app and exposes it through a Gateway that runs on an ELB for Envoy proxy. You grant the controller permissions, install it alongside Envoy Gateway, and then create an EnvoyProxy and a GatewayClass, an echo backend, a Gateway and an HTTPRoute, and an ELBProxyConfiguration that tells the controller to create a proxy for the Gateway.

## Prerequisites
<a name="kubernetes-get-started-prerequisites"></a>

Before you begin, make sure that you have the following:
+ An Amazon EKS cluster with Envoy Gateway installed, on a Kubernetes version that your Envoy Gateway release supports.
+ The `kubectl`, `helm`, and `eksctl` command line tools, and AWS credentials configured for your cluster's account.
+ Pod IPs that are routable in the VPC, for example with the Amazon VPC CNI.
+ At least two subnets in different Availability Zones, tagged `kubernetes.io/role/elb=1`. The controller uses this tag to discover subnets for an internet-facing proxy, which is what this walkthrough creates. For an internal proxy, tag the subnets `kubernetes.io/role/internal-elb` instead.
+ A proxy role whose ARN you set as `roleArn`. The proxy uses this role to publish logs to CloudWatch Logs and when Envoy filters or extensions call AWS services. To create it, see [Create a proxy role](setting-up.md#setting-up-proxy-role).

## Step 1: Grant the controller permissions
<a name="kubernetes-get-started-permissions"></a>

The controller runs in the Envoy Gateway pod and uses its ServiceAccount. Create the controller's IAM policy from the `iam-policy.json` file in the [project repository](https://github.com/aws/elb-envoy-remote-infra-provider), and then attach it to that ServiceAccount with IAM Roles for Service Accounts (IRSA).

**To grant the controller permissions**
+ Bind the policy to the Envoy Gateway ServiceAccount.

  ```
  eksctl create iamserviceaccount --cluster my-cluster \
    --namespace envoy-gateway-system --name envoy-gateway \
    --attach-policy-arn arn:aws:iam::<ACCOUNT_ID>:policy/ELBProxyControllerPolicy \
    --override-existing-serviceaccounts --approve
  ```

Replace {{my-cluster}} with your cluster name and {{ACCOUNT\_ID}} with your account ID.

## Step 2: Install the controller
<a name="kubernetes-get-started-install"></a>

Install the controller with Helm into the `envoy-gateway-system` namespace.

**To install the controller**

1. Install the Helm chart.

   ```
   helm install elb-envoy-remote-infra-provider \
     oci://public.ecr.aws/aws-elb-proxy/elb-envoy-remote-infra-provider-chart \
     -n envoy-gateway-system \
     --set clusterName=my-cluster --set aws.region=us-east-1 --set aws.vpcId=<VPC_ID>
   ```

1. Set Envoy Gateway's infrastructure provider to `Remote` so that it delegates proxy creation to the controller, and then restart Envoy Gateway so the sidecar is injected.

   ```
   provider:
     type: Custom
     custom:
       resource:
         type: Kubernetes
       infrastructure:
         type: Remote
         remote:
           service:
             unix:
               path: /var/run/elb-envoy-remote-infra-provider/server.sock
   ```

Replace {{my-cluster}}, the region, and {{VPC\_ID}} with your values.

## Step 3: Create the EnvoyProxy and GatewayClass
<a name="kubernetes-get-started-envoyproxy"></a>

The GatewayClass belongs to Envoy Gateway, not to the controller. It points at an EnvoyProxy that disables access logging. Envoy Gateway's default access log writes to a file sink, which the proxy rejects, so this EnvoyProxy sets `telemetry.accessLog.disable: true`.

**To create the EnvoyProxy and GatewayClass**

1. Save the following as `gatewayclass.yaml`.

   ```
   apiVersion: gateway.envoyproxy.io/v1alpha1
   kind: EnvoyProxy
   metadata:
     name: elb-proxy
     namespace: envoy-gateway-system
   spec:
     ipFamily: IPv4
     telemetry:
       accessLog:
         disable: true
   ---
   apiVersion: gateway.networking.k8s.io/v1
   kind: GatewayClass
   metadata:
     name: elb-proxy-aws
   spec:
     controllerName: gateway.envoyproxy.io/gatewayclass-controller
     parametersRef:
       group: gateway.envoyproxy.io
       kind: EnvoyProxy
       name: elb-proxy
       namespace: envoy-gateway-system
   ```

1. Apply the file.

   ```
   kubectl apply -f gatewayclass.yaml
   ```

## Step 4: Deploy the echo backend
<a name="kubernetes-get-started-backend"></a>

Deploy a sample echo app as the backend for the Gateway.

**To deploy the echo backend**

1. Save the following as `echo.yaml`.

   ```
   apiVersion: v1
   kind: Namespace
   metadata:
     name: echo
   ---
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: echo
     namespace: echo
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: echo
     template:
       metadata:
         labels:
           app: echo
       spec:
         containers:
         - name: echo
           image: registry.k8s.io/gateway-api/echo-basic:v1.5.1
           ports:
           - containerPort: 3000
   ---
   apiVersion: v1
   kind: Service
   metadata:
     name: echo
     namespace: echo
   spec:
     selector:
       app: echo
     ports:
     - name: http
       port: 8080
       targetPort: 3000
   ```

1. Apply the file.

   ```
   kubectl apply -f echo.yaml
   ```

## Step 5: Create the Gateway and HTTPRoute
<a name="kubernetes-get-started-gateway"></a>

Create a Gateway that uses the GatewayClass from Step 3, and an HTTPRoute that sends traffic to the echo backend.

**To create the Gateway and HTTPRoute**

1. Save the following as `gateway.yaml`.

   ```
   apiVersion: gateway.networking.k8s.io/v1
   kind: Gateway
   metadata:
     name: echo-gateway
     namespace: echo
   spec:
     gatewayClassName: elb-proxy-aws
     listeners:
     - name: http
       protocol: HTTP
       port: 80
       allowedRoutes:
         namespaces:
           from: Same
   ---
   apiVersion: gateway.networking.k8s.io/v1
   kind: HTTPRoute
   metadata:
     name: echo
     namespace: echo
   spec:
     parentRefs:
     - name: echo-gateway
     rules:
     - matches:
       - path:
           type: PathPrefix
           value: /
       backendRefs:
       - name: echo
         port: 8080
   ```

1. Apply the file.

   ```
   kubectl apply -f gateway.yaml
   ```

**Note**
The Gateway doesn't get an address yet. The controller creates a proxy only for a Gateway that has an ELBProxyConfiguration attached.

## Step 6: Attach an ELBProxyConfiguration
<a name="kubernetes-get-started-elbproxyconfig"></a>

The ELBProxyConfiguration tells the controller to create a proxy for the Gateway. Create it in the same namespace as the Gateway. Without an ELBProxyConfiguration, the Gateway gets no proxy.

**To attach an ELBProxyConfiguration**

1. Save the following as `proxy.yaml`. The example sets `internet-facing` so that you can reach the proxy from your machine. You must quote the `"off"` value, so that it isn't read as a boolean.

   ```
   apiVersion: gateway.elbproxy.aws/v1alpha1
   kind: ELBProxyConfiguration
   metadata:
     name: echo-proxy
     namespace: echo
   spec:
     targetRefs:
     - group: gateway.networking.k8s.io
       kind: Gateway
       name: echo-gateway
     roleArn: ${PROXY_ROLE_ARN}
     networkConfiguration:
       ipConfiguration:
         ipAddressingConfiguration:
           ipv4Addressability: internet-facing
           ipv6Addressability: "off"
   ```

1. Set the role ARN, and then apply the file. Replace the example ARN with your own proxy role ARN.

   ```
   export PROXY_ROLE_ARN=arn:aws:iam::123456789012:role/my-proxy-role
   envsubst < proxy.yaml | kubectl apply -f -
   ```

## Step 7: Wait for the Gateway
<a name="kubernetes-get-started-wait"></a>

Provisioning the proxy takes several minutes. Wait for the Gateway to become `Programmed`.

**To wait for the Gateway**
+ Run the following command.

  ```
  kubectl wait gateway/echo-gateway -n echo \
    --for=condition=Programmed --timeout=15m
  ```

## Step 8: Send a request
<a name="kubernetes-get-started-request"></a>

The Gateway's address is the proxy's DNS name. Send a request to it.

**To send a request**
+ Get the Gateway address, and then send a request.

  ```
  export GATEWAY_HOST=$(kubectl get gateway echo-gateway -n echo \
    -o jsonpath='{.status.addresses[0].value}')
  curl -i http://$GATEWAY_HOST/
  ```

The echo server replies with JSON that includes the pod name and namespace. The DNS name can take a few minutes to resolve after the proxy is created.

## Clean up
<a name="kubernetes-get-started-cleanup"></a>

Delete the Gateway first, so that the controller removes the proxy and the security groups that it created. Then delete the rest.

```
kubectl delete -f gateway.yaml
kubectl delete -f proxy.yaml
kubectl delete -f echo.yaml
kubectl delete -f gatewayclass.yaml
```

For the full installation guide, the configuration reference, and the compatibility matrix of supported Envoy Gateway, Gateway API, and Kubernetes versions, see the [elb-envoy-remote-infra-provider project on GitHub](https://github.com/aws/elb-envoy-remote-infra-provider).

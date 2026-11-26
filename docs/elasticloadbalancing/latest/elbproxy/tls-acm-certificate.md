---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/tls-acm-certificate.html
---

# Terminate TLS with an ACM certificate

With Elastic Load Balancing for Envoy (ELB for Envoy), you can terminate TLS on your proxy with a certificate from AWS Certificate Manager (ACM). You associate the certificate with the proxy, then update the proxy configuration so that a listener references the certificate by its ARN. The proxy supplies the certificate at runtime, so you don't embed the private key in your configuration.

## Prerequisites
<a name="tls-acm-prerequisites"></a>

Before you terminate TLS with an ACM certificate, make sure that you have the following:
+ A certificate in ACM, in the same account and AWS Region as the proxy.
+ The ARN of an existing proxy.
+ Permission to call `acm:CreateCertificateRelation` on the certificate. ELB for Envoy associates the certificate using your credentials.

## Associate the certificate
<a name="tls-acm-associate"></a>

Associate the certificate with your proxy using the console or the AWS CLI. Choose the tab for the method that you want to use. You can't associate a certificate by using CloudFormation. The association starts in the `associate-in-progress` state. When its status is `active`, the certificate is available to the proxy and you can reference it in your configuration.

------
#### [ Console ]

**To associate a certificate with a proxy**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Proxies**.

1. Choose the proxy that you want to update to open its details page.

1. Choose the **Certificates** tab.

1. Choose **Associate certificates**.

1. In the **Certificates** table, select the certificates that you want to associate.

1. Choose **Save changes**.

To confirm the association, verify that the certificate appears in the **Already-associated certificates** section of the **Certificates** tab.

------
#### [ AWS CLI ]

To associate a certificate, run the **associate-certificate** command.

```
aws elb-proxy associate-certificate \
  --proxy-identifier <proxy-arn> \
  --certificate-identifier arn:aws:acm:us-east-1:123456789012:certificate/11111111-2222-3333-4444-555555555555
```

Replace {{proxy-arn}} with the ARN of your proxy, and replace the example certificate ARN with the ARN of your certificate.

To check the status of the association, run the **list-certificate-associations** command until the status is `active`.

```
aws elb-proxy list-certificate-associations --proxy-identifier <proxy-arn>
```

Replace {{proxy-arn}} with the ARN of your proxy. The response lists each certificate association and its status.

------

## Reference the certificate in a listener
<a name="tls-acm-reference"></a>

After the certificate association is `active`, reference the certificate in the listener's `DownstreamTlsContext`. Name the certificate by its ARN in `common_tls_context.tls_certificate_sds_secret_configs`. ELB for Envoy supplies the certificate, so the entry has no `sds_config`.

Fragment:

```
transport_socket:
  name: envoy.transport_sockets.tls
  typed_config:
    "@type": type.googleapis.com/envoy.extensions.transport_sockets.tls.v3.DownstreamTlsContext
    common_tls_context:
      tls_certificate_sds_secret_configs:
      - name: "arn:aws:acm:us-east-1:123456789012:certificate/11111111-2222-3333-4444-555555555555"
```

Replace the example certificate ARN with the ARN of your associated certificate.

After you update the listener, apply the updated configuration. For instructions, see [Update a proxy configuration](update-proxy-configuration.md).

## Complete sample configuration
<a name="tls-acm-sample"></a>

The following Envoy configuration listens on port 443, terminates TLS with an ACM certificate, and responds with a fixed string. Associate the certificate with your proxy before you apply the configuration.

```
admin:
  address:
    socket_address:
      address: 127.0.0.1
      port_value: 9901

static_resources:
  listeners:
  - name: https_listener
    address:
      socket_address:
        address: 0.0.0.0
        port_value: 443
    filter_chains:
    - transport_socket:
        name: envoy.transport_sockets.tls
        typed_config:
          "@type": type.googleapis.com/envoy.extensions.transport_sockets.tls.v3.DownstreamTlsContext
          common_tls_context:
            tls_certificate_sds_secret_configs:
            - name: "arn:aws:acm:us-east-1:123456789012:certificate/11111111-2222-3333-4444-555555555555"
      filters:
      - name: envoy.filters.network.http_connection_manager
        typed_config:
          "@type": type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager
          stat_prefix: ingress_https
          route_config:
            name: local_route
            virtual_hosts:
            - name: local_service
              domains: ["*"]
              routes:
              - match:
                  prefix: "/"
                direct_response:
                  status: 200
                  body:
                    inline_string: "Your proxy is running with an ACM certificate\n"
          http_filters:
          - name: envoy.filters.http.router
            typed_config:
              "@type": type.googleapis.com/envoy.extensions.filters.http.router.v3.Router
```

Replace the example certificate ARN with the ARN of your associated certificate.

## Test the certificate
<a name="tls-acm-test"></a>

To test the proxy, send a request for a domain name on your certificate with the following **curl** command. The `--connect-to` option sends the request to the proxy without a DNS change.

```
curl -v --connect-to www.example.com:443:<proxy-dns-name>:443 https://www.example.com/
```

Replace {{www.example.com}} with a domain name on your certificate, and replace {{proxy-dns-name}} with the proxy's `dnsName` from **get-proxy**.

The output includes the certificate the proxy presents and the response.

```
* Server certificate:
*   subject: CN=www.example.com
*   subjectAltName: "www.example.com" matches cert's "www.example.com"
< HTTP/1.1 200 OK
< content-length: 46
< content-type: text/plain
< server: envoy
Your proxy is running with an ACM certificate
```

## Disassociate the certificate
<a name="tls-acm-disassociate"></a>

When you no longer need a certificate on your proxy, disassociate it using the console or the AWS CLI. Choose the tab for the method that you want to use. You can't disassociate a certificate by using CloudFormation.

------
#### [ Console ]

**To disassociate certificates from a proxy**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Proxies**.

1. Choose the proxy that you want to update to open its details page.

1. Choose the **Certificates** tab.

1. Select the certificates that you want to remove. You can select more than one.

1. Choose **Disassociate**.

1. In the confirmation dialog box, do one of the following:
   + If you selected one certificate, choose **Disassociate**.
   + If you selected more than one certificate, enter **confirm** in the text field, and then choose **Disassociate**.

The console disassociates each selected certificate and shows which ones succeeded and which failed.

------
#### [ AWS CLI ]

To disassociate a certificate, run the **disassociate-certificate** command.

```
aws elb-proxy disassociate-certificate \
  --proxy-identifier <proxy-arn> \
  --certificate-identifier <certificate-arn>
```

Replace {{proxy-arn}} with the ARN of your proxy, and replace {{certificate-arn}} with the ARN of the certificate that you want to remove.

------

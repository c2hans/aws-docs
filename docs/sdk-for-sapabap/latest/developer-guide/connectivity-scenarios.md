---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/connectivity-scenarios.html
---

# Advanced connectivity scenarios
<a name="connectivity-scenarios"></a>

AWS SDK for SAP ABAP consumes AWS services by making HTTPS calls to AWS endpoints. In general, AWS endpoints are accessible over the internet. An SAP system must be able to reach out to the internet to establish these outbound connections. SDK for SAP ABAP never requires an inbound connection from the internet into the SAP system.

The following scenarios offer different ways to establish the outbound connection.

**Topics**
+ [Connection through a proxy server](#proxy-server)
+ [Connection through a packet inspecting firewall](#packet-firewall)
+ [Gateway endpoints](#gateway-endpoints)
+ [Custom interface endpoints](#interface-endpoints)
+ [Advanced routing](#advanced-routing)
+ [Per-service proxy server override](#proxy-server-override)
+ [Accessing endpoints in multiple Regions](#multiple-regions)

## Connection through a proxy server
<a name="proxy-server"></a>

To establish a connection through a proxy server, use the following steps.

1. In the SDK, go to Transaction **`SICF`**.

1. Choose **Execute**.

1. In the menu, choose **Client** > **Proxy server**.

1. Set **Proxy setting** as **Active**.

1. In the field for **No Proxy for the Following Addresses**, list any exceptions separated by semicolons.

1. In the **HTTP Protocol** and **HTTPs Protocol** fields, specify the connection details for your proxy server.

The SDK is unaware of the proxy server, and does not require any settings to use the SAP system's proxy server configuration.

**Note**
If you use [Amazon EC2 instance metadata authentication](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/system-authentication.html#metadata-authentication), then the SAP system cannot use the proxy server to access the local instance metadata at `http://169.254.169.254`. You must include `169.254.169.254` in the field for *No Proxy for the Following Addresses*.

**Note**
You can override the proxy server behavior on a per-service basis in the **Advanced Routing** section of `/AWS1/IMG`. For more information, see [Per-service proxy server override](#proxy-server-override).

## Connection through a packet inspecting firewall
<a name="packet-firewall"></a>

You can configure a packet inspecting firewall for outbound connection. These firewalls decrypt the SSL traffic, and then re-encrypt it before passing it on to the endpoint. This configuration usually requires the firewall to issue its own certificates to the SAP system that is consuming an AWS service. You must install your firewall’s CA certificate in `STRUST`. For more information, see [HTTPS connectivity](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/prerequisites.html#https-connectivity).

## Gateway endpoints
<a name="gateway-endpoints"></a>

Some AWS services offer gateway endpoints to provide a VPC with high-performance access without internet. These endpoints are transparent to SDK for SAP ABAP, and do not require any configuration.

For more information, see [Gateway endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html).

## Custom interface endpoints
<a name="interface-endpoints"></a>

If you need to override the default endpoint resolution with a custom endpoint, you can use an interface endpoint to provide your VPC with high-performance access without internet. For more information, see [Configure an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/interface-endpoints.html).

When not using private DNS, these endpoints have their own DNS addresses, and an ABAP program must explicitly override the usual endpoint resolution logic. For more information, see AWS re:Post – [Why can't I resolve service domain names for an interface VPC endpoint?](https://repost.aws/knowledge-center/vpc-interface-configure-dns)

In the following example, an interface endpoint is created for AWS STS and Amazon Translate. The SAP system is not using private DNS, and calls the services with custom endpoint. The logical resources defined in `/AWS1/IMG` represent the physical interface endpoint addresses, such as `vpce-0123456789abcdef-hd52vxz.translate.us-west-2.vpce.amazonaws.com`. This avoids hard coding the DNS in code.

In the following code, the logical resources in `/AWS1/IMG` are first resolved to physical endpoint names. They are then provided to the factory methods of AWS session class (that uses AWS STS to assume an IAM role) and translate API class.

```
" This example assumes we have defined our logical endpoints in /AWS1/IMG
" as logical resources so that we don't hardcode our endpoints in code.
" The endpoints may be different in Dev, QA and Prod environments.
DATA(lo_config) = /aws1/cl_rt_config=>create( 'DEMO' ).
DATA(lo_resolver) = /aws1/cl_rt_lresource_resolver=>create( lo_config ).

" logical resource STS_ENDPOINT should resolve to the interface endpoint
" for example vpce-0123456789-abcdefg.sts.us-west-2.vpce.amazonaws.com
DATA(lv_sts_endpoint) = lo_resolver->resolve_lresource( 'STS_ENDPOINT' ).

" logical resource XL8_ENDPOINT should resolve to the interface endpoint
" e.g. vpce-0123456789abcdefg-12345567.translate.us-west-2.vpce.amazonaws.com
DATA(lv_xl8_endpoint) = lo_resolver->resolve_lresource( 'XL8_ENDPOINT' ).

" the session itself uses the sts service to assume a role, so the
" session creation process requires a custom endpoint, specified here
DATA(lo_session) = /aws1/cl_rt_session_aws=>create(
  iv_profile_id = 'DEMO'
  iv_custom_sts_endpoint = |https://{ lv_sts_endpoint }|
).

" now we create an API object, and override the default endpoint with
" the custom endpoint
DATA(lo_xl8)     = /aws1/cl_xl8_factory=>create(
  io_session = lo_session
  iv_custom_endpoint = |https://{ lv_xl8_endpoint }| " provide custom endpoint
).
" now calls to lo_xl8 go to custom endpoint...
```

As shown in the example, any method calls on `go_xl8` go to the endpoint `https://vpce-0123456789abcdefg-12345567.translate.us-west-2.vpce.amazonaws.com`. It is also possible to define the routing custom endpoint in the IMG configuration instead of in code, as shown in the next section.

## Advanced routing
<a name="advanced-routing"></a>

 In the previous section we showed how a custom endpoint can be specified in the `iv_custom_endpoint` argument of the factory methods for the SDK modules. As the number of ABAP programs using the SDK increases, this can become difficult to manage. It is possible to configure a mapping from an AWS service to a custom endpoint in the SDK Profile. For each SID, client, and scenario, the service three-letter abbreviation (TLA) can be mapped to an endpoint URL:

|  TLA  |  Custom Endpoint URL  |
| --- | --- |
| BDR | https://vpce-23456789abcdef012-3c4d5e6f.bedrock-runtime.us-east-1.vpce.amazonaws.com |
| LMD | https://vpce-123456789abcdef01-2b3c4d5e.lambda.us-east-1.vpce.amazonaws.com |
| S3 | https://vpce-0123456789abcdef0-1a2b3c4d.s3.us-east-1.vpce.amazonaws.com |

 With this configuration, you do not need to specify `iv_custom_endpoint` in the factory method calls. The custom endpoint is selected automatically from the configuration table. The configuration is specific to the SDK Profile so you can create multiple profiles with different routing to suit your needs. As with other SDK Profile configuration, the routing is SID and client specific so separate routing can be defined for different systems.

## Per-service proxy server override
<a name="proxy-server-override"></a>

By default, the SDK uses the proxy server settings configured in Transaction `SICF` (see [Connection through a proxy server](#proxy-server)). The proxy settings in `SICF` apply globally to all outbound HTTP connections from the SAP system. In some environments, you may need finer control over which AWS services use the proxy server and which connect directly.

In the **Advanced Routing** section of `/AWS1/IMG`, you can configure a **Use Proxy Server** setting for each service. This setting controls whether the SDK routes requests for that service through the proxy server defined in `SICF`, regardless of the global proxy activation or filter settings.

The following values are available:
+ **Default** – Use whatever proxy behavior is configured in `SICF`. If the proxy is active and the endpoint is not excluded by the filter, the proxy is used. This is the default behavior.
+ **Always** – Always route requests for this service through the proxy server defined in `SICF`, regardless of the global activation or filter settings.
+ **Never** – Never route requests for this service through the proxy server, regardless of the global activation or filter settings. Use this when a service endpoint is reachable directly without a proxy, for example when using a VPC endpoint.

For example, you might configure Amazon S3 and AWS STS to never use the proxy (because they are accessed through VPC gateway endpoints), while Amazon SNS always uses the proxy because it is only reachable through the internet.

| TLA | Use Proxy Server |
| --- | --- |
| EC2 | Default |
| S3 | Never |
| SNS | Always |
| STS | Never |

This configuration is defined per SDK Profile, SID, client, and scenario. You can create multiple profiles with different proxy routing to suit different environments or use cases.

**Note**
The proxy server host and port are always defined in the **HTTPS Protocol** tab of the proxy settings in Transaction `SICF`. The per-service override only controls whether the proxy is used, not which proxy server is used.

## Accessing endpoints in multiple Regions
<a name="multiple-regions"></a>

AWS endpoint is automatically determined from your default AWS Region that is defined in the SDK profile. You can also specify a region programmatically, overriding the default region. This can be overridden in the factory `CREATE()` method, or later with the SDK’s configuration object. For more information, see [Programmatic configuration](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/features.html#programmatic-configuration).

In the following example, the factory `CREATE()` method is used to set the region and list the Amazon SQS queues in both `us-east-1` and `us-west-2` Regions.

```
REPORT zdemo_sqs_queue_list.
parameters: profile type /AWS1/RT_PROFILE_ID OBLIGATORY.

START-OF-SELECTION.
DATA(go_session) = /aws1/cl_rt_session_aws=>create( profile ).
data(lt_region) = VALUE stringtab(
  ( |us-east-1| )
  ( |us-west-2| )
).

LOOP AT lt_region INTO DATA(lv_region).
  DATA(go_sqs)  = /aws1/cl_sqs_factory=>create(
    io_session = go_session
    iv_region = conv /AWS1/RT_REGION_ID( lv_region )
  ).
  WRITE: / lv_region COLOR COL_HEADING.
  LOOP AT go_sqs->listqueues( )->get_queueurls( ) INTO DATA(lo_url).
    WRITE: / lo_url->get_value( ).
  ENDLOOP.
ENDLOOP.
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for SAP ABAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-sapabap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingproxy-proxy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingProxy::Proxy

Creates an Elastic Load Balancing for Envoy proxy. A proxy serves as the single point of contact for your clients. It runs your Envoy configuration, and Elastic Load Balancing for Envoy scales it as your traffic changes.

Elastic Load Balancing for Envoy provisions and scales the proxy, patches the operating system, and monitors the proxy's health. Because the proxy runs in your virtual private cloud (VPC), you keep control of your network, security groups, and AWS Identity and Access Management (IAM) permissions.

When you create a proxy, Elastic Load Balancing for Envoy provisions a dedicated DNS name for it and runs the configuration that you provide.

If you update a property that requires replacement, CloudFormation deletes the existing proxy before it creates the new one, because the proxy name must be unique in your AWS account for the Region. The proxy isn't available during the replacement. If deletion protection is turned on, the replacement fails.

When you update `ConfigurationFile`, `ConfigurationArchive`, or `CustomerKmsKeyArn`, the stack update completes as soon as Elastic Load Balancing for Envoy accepts the new configuration. It doesn't wait for the proxy to apply the configuration. The proxy nodes can still reject the configuration. For example, the configuration file might reference a file that isn't in the configuration archive. If the nodes reject it, they keep serving the previous configuration, and CloudFormation doesn't roll back the stack.

The outcome then depends on whether the proxy has an earlier configuration that the nodes applied and that uses the same customer managed key. If it does, Elastic Load Balancing for Envoy rolls the proxy back to that configuration, and the proxy status stays `active`. Otherwise, such as the first configuration update after you create the proxy, the proxy status changes to `action-required`. The `status.reasons` field then includes the reason code `InvalidCustomerConfigurationContents` with the error message. The status returns to `active` after a valid configuration is applied.

To confirm that an update took effect, call the [ListProxyUpdates](https://docs.aws.amazon.com/elasticloadbalancing/elb-proxy/latest/APIReference/API_ListProxyUpdates.html) operation. Check the `validationStatus` and `propagationStatus` of the most recent update. For a rejected update, `validationStatus` is `invalid` and `propagationStatus` is `failed`. To see `status.reasons`, call the [GetProxy](https://docs.aws.amazon.com/elasticloadbalancing/elb-proxy/latest/APIReference/API_GetProxy.html) operation.

Drift detection doesn't check `ConfigurationFile` or `ConfigurationArchive`. Changes to the configuration that you make outside CloudFormation aren't reported as drift. For `Attributes`, drift detection compares only the attribute keys that your template specifies. For more information, see [Detect unmanaged configuration changes to stacks and resources with drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html) in the *CloudFormation User Guide*.

For more information, see [What is Elastic Load Balancing for Envoy?](https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/what-is.html) and [Create a proxy](https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/create-proxy.html) in the *Elastic Load Balancing for Envoy User Guide*.

## Syntax
<a name="aws-resource-elasticloadbalancingproxy-proxy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-elasticloadbalancingproxy-proxy-syntax.json"></a>

```json
{
  "Type" : "AWS::ElasticLoadBalancingProxy::Proxy",
  "Properties" : {
      "[Attributes](#cfn-elasticloadbalancingproxy-proxy-attributes)" : {{[ Attribute, ... ]}},
      "[ConfigurationArchive](#cfn-elasticloadbalancingproxy-proxy-configurationarchive)" : {{ConfigurationArchive}},
      "[ConfigurationFile](#cfn-elasticloadbalancingproxy-proxy-configurationfile)" : {{ConfigurationFile}},
      "[CustomerKmsKeyArn](#cfn-elasticloadbalancingproxy-proxy-customerkmskeyarn)" : {{String}},
      "[IpAddressingConfiguration](#cfn-elasticloadbalancingproxy-proxy-ipaddressingconfiguration)" : {{IpAddressingConfiguration}},
      "[Name](#cfn-elasticloadbalancingproxy-proxy-name)" : {{String}},
      "[ProxyVersion](#cfn-elasticloadbalancingproxy-proxy-proxyversion)" : {{String}},
      "[RoleArn](#cfn-elasticloadbalancingproxy-proxy-rolearn)" : {{String}},
      "[SecurityGroups](#cfn-elasticloadbalancingproxy-proxy-securitygroups)" : {{[ String, ... ]}},
      "[Subnets](#cfn-elasticloadbalancingproxy-proxy-subnets)" : {{[ String, ... ]}},
      "[Tags](#cfn-elasticloadbalancingproxy-proxy-tags)" : {{[ Tag, ... ]}},
      "[Type](#cfn-elasticloadbalancingproxy-proxy-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-elasticloadbalancingproxy-proxy-syntax.yaml"></a>

```yaml
Type: AWS::ElasticLoadBalancingProxy::Proxy
Properties:
  [Attributes](#cfn-elasticloadbalancingproxy-proxy-attributes): {{
    - Attribute}}
  [ConfigurationArchive](#cfn-elasticloadbalancingproxy-proxy-configurationarchive): {{
    ConfigurationArchive}}
  [ConfigurationFile](#cfn-elasticloadbalancingproxy-proxy-configurationfile): {{
    ConfigurationFile}}
  [CustomerKmsKeyArn](#cfn-elasticloadbalancingproxy-proxy-customerkmskeyarn): {{String}}
  [IpAddressingConfiguration](#cfn-elasticloadbalancingproxy-proxy-ipaddressingconfiguration): {{
    IpAddressingConfiguration}}
  [Name](#cfn-elasticloadbalancingproxy-proxy-name): {{String}}
  [ProxyVersion](#cfn-elasticloadbalancingproxy-proxy-proxyversion): {{String}}
  [RoleArn](#cfn-elasticloadbalancingproxy-proxy-rolearn): {{String}}
  [SecurityGroups](#cfn-elasticloadbalancingproxy-proxy-securitygroups): {{
    - String}}
  [Subnets](#cfn-elasticloadbalancingproxy-proxy-subnets): {{
    - String}}
  [Tags](#cfn-elasticloadbalancingproxy-proxy-tags): {{
    - Tag}}
  [Type](#cfn-elasticloadbalancingproxy-proxy-type): {{String}}
```

## Properties
<a name="aws-resource-elasticloadbalancingproxy-proxy-properties"></a>

`Attributes`  <a name="cfn-elasticloadbalancingproxy-proxy-attributes"></a>
The proxy attributes, as a list of key-value pairs. Attributes are optional settings that control secondary proxy behavior. Core behavior, such as networking and the Envoy configuration, is set through other properties.
Each attribute has a default value that applies unless you set the attribute. If you remove an attribute from your template, CloudFormation resets it to its default value. If you change an attribute outside CloudFormation, the next stack update that changes a property other than `Tags` restores your template's value. An update that changes only tags doesn't. Some attributes can be set only when you create the proxy. Changing or removing one of these attributes after the proxy is created fails. The supported attribute keys are the following:
+ `deletion_protection.enabled` – Specifies whether to prevent the proxy from being deleted accidentally (`true` or `false`). If you turn on deletion protection, you must turn it off before you can delete the proxy. The default is `false`. While deletion protection is on, CloudFormation can't delete the proxy, so stack deletion and any update that requires replacement fail.
+ `ddos_protection.syn_cookie.mode` – How the proxy applies SYN cookie mitigations for SYN flood protection. `reactive` turns on mitigation only when a SYN flood is detected, `continuous` keeps it on, and `off` disables it. The default is `reactive`.
+ `envoy.log_level` – The log level for the Envoy process. Valid values are `off`, `critical`, `error`, `warning` (or its alias `warn`), `info`, `debug`, and `trace`. The default is `warn`.
+ `envoy.component_log_level` – Per-component log level overrides for Envoy, as a comma-separated list of `component:level` pairs (for example, `http:debug,router:debug`). Levels use the same values as `envoy.log_level`. Components that you don't specify use the level set by `envoy.log_level`. An empty value clears all per-component overrides. The default is empty.
+ `waf.fail_open.enabled` – Specifies whether to allow traffic through when AWS WAF is unavailable (`true` or `false`). When `false`, requests are blocked if AWS WAF is unavailable. The default is `false`.
+ `waf.web_acl_arn` – The ARN of the regional AWS WAF web ACL to associate with the proxy. If you leave it empty, the proxy has no web ACL. The default is empty.

  You can set this attribute when you create the proxy, and you can create the web ACL in the same stack. After creation, you can't change or remove it with a stack update, and the update fails if you try.

  To change or remove the web ACL after creation, use AWS WAF instead. To change it, call the AWS WAF [AssociateWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_AssociateWebACL.html) operation with the proxy ARN. To remove it, call [DisassociateWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_DisassociateWebACL.html). AWS WAF is the source of truth for the association.

  To manage the proxy's web ACL in your template instead, leave `waf.web_acl_arn` out of the proxy and use the [AWS::WAFv2::WebACLAssociation](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wafv2-webaclassociation.html) resource with the proxy ARN as `ResourceArn`. You can then change or remove the web ACL with stack updates, and drift detection stays in sync. Use only one of these methods for a proxy, either `waf.web_acl_arn` or an `AWS::WAFv2::WebACLAssociation`, not both. For an example, see "Example - Associate an AWS WAF web ACL with a proxy."

  To set this attribute, you need the `wafv2:AssociateWebACL` permission on the web ACL. Creating a proxy with a web ACL, and `AssociateWebACL`, also require `elasticloadbalancing:CreateProxyWafAssociation` on the proxy. `DisassociateWebACL` requires `elasticloadbalancing:DeleteProxyWafAssociation`, `GetWebACLForResource` requires `elasticloadbalancing:GetProxyWafAssociation`, and `ListResourcesForWebACL` requires `elasticloadbalancing:ListProxyWafAssociations`.

  After you change or remove the web ACL in AWS WAF, the following conditions and outcomes apply:
  + `waf.web_acl_arn` value – The attribute shows the new ARN, or an empty string.
  + Drift detection – If your template specifies `waf.web_acl_arn`, the proxy's `Attributes` show as modified until you update the template.
  + Clearing drift – Set `waf.web_acl_arn` in your template to the new ARN, or an empty string, after the change in AWS WAF.
  + Unrelated updates – Updates that don't change `waf.web_acl_arn` succeed while the template is out of date.
  + Removing the key – If you remove `waf.web_acl_arn` from your template, the update fails.
  + Changing the value – If you change `waf.web_acl_arn` in your template to a value other than the web ACL associated in AWS WAF, the update fails.
  + Failed rollback – If your template is already out of date when you remove or change `waf.web_acl_arn`, the rollback also fails and the stack is left in the `UPDATE_ROLLBACK_FAILED` state. To recover, do the following:

    1. Continue the rollback and skip the proxy's logical ID. For more information, see [Continue rolling back an update](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html) in the *CloudFormation User Guide*.

    1. Set `waf.web_acl_arn` in your template to the web ACL associated in AWS WAF, and update the stack.
For more information, see [Proxy attributes](https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/proxy-attributes.html) and [Protect a proxy with AWS WAF](https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/waf.html) in the *Elastic Load Balancing for Envoy User Guide*.
*Required*: No
*Type*: Array of [Attribute](aws-properties-elasticloadbalancingproxy-proxy-attribute.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConfigurationArchive`  <a name="cfn-elasticloadbalancingproxy-proxy-configurationarchive"></a>
The configuration archive for the proxy. The archive is a ZIP file of the supporting files that your configuration file references, such as certificates, response bodies, or xDS seed files. Omit it if your configuration file references no external files.
Elastic Load Balancing for Envoy extracts the archive into the directory that Envoy sees as its filesystem root. A file named `envoy.yaml` at the archive root is ignored. The configuration file is always the bootstrap configuration.
If you remove the archive from your template, CloudFormation removes it from the proxy. Updating the archive doesn't replace the proxy.
CloudFormation can't create a ZIP archive from files. Create the archive outside CloudFormation, base64-encode it, and specify the encoded string in the `ConfigurationBytes` subproperty of `ConfigurationArchive`.
Base64 encoding makes the archive about 33% larger, and the encoded archive counts toward the template size. A template stored in Amazon S3 can be at most 1 MB. If you pass the archive as a template parameter, the parameter value can be at most 4,096 bytes. As a result, an archive that you specify through CloudFormation must be much smaller than the 10 MB archive quota.
The configuration archive behaves the same way as `ConfigurationFile` for drift detection and stack updates. For that guidance, see the `ConfigurationFile` property.
For more information, see [Configuration archive](https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/how-envoy-runs.html#how-envoy-runs-archive) in the *Elastic Load Balancing for Envoy User Guide*.
*Required*: No
*Type*: [ConfigurationArchive](aws-properties-elasticloadbalancingproxy-proxy-configurationarchive.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConfigurationFile`  <a name="cfn-elasticloadbalancingproxy-proxy-configurationfile"></a>
The configuration file for the proxy. The configuration file is your Envoy bootstrap configuration, in YAML format.
Although this property is shown as not required, you must specify it when you create a proxy. If you omit it, the create fails. You also can't remove it from your template later. An update without it fails. Elastic Load Balancing for Envoy validates the configuration file against the Envoy bootstrap schema of the proxy version.
In a template, you can write the configuration file inline and encode it with the [Fn::Base64](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-base64.html) intrinsic function, as shown in the examples. The configuration counts toward the template size: CloudFormation accepts templates of up to 51,200 bytes when you pass the template body directly, and up to 1 MB when you store the template in Amazon S3. For a large configuration file, store the template in Amazon S3. For more information, see [CloudFormation quotas](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html) in the *CloudFormation User Guide*.
Reference an ACM certificate in the configuration file only after the certificate is associated with the proxy. For more information about certificate associations, see [AWS::ElasticLoadBalancingProxy::CertificateAssociation](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingproxy-certificateassociation.html).
If you change the proxy's configuration outside CloudFormation, the following conditions and outcomes apply:
+ Drift detection – If you change the configuration file or configuration archive outside CloudFormation, drift detection doesn't report the change. Elastic Load Balancing for Envoy doesn't return these properties. For example, you might change them with the [UpdateProxyConfiguration](https://docs.aws.amazon.com/elasticloadbalancing/elb-proxy/latest/APIReference/API_UpdateProxyConfiguration.html) operation.
+ Stack updates – A stack update doesn't restore your template's configuration unless your template's `ConfigurationFile`, `ConfigurationArchive`, or `CustomerKmsKeyArn` changes. When one of them changes, the template's configuration replaces the configuration on the proxy, including any changes you made outside CloudFormation.
To find out whether the proxy's configuration differs from your template, compare file hashes. The `GetProxy` operation returns `configFileHash` and `configArchiveHash` in `configurationMetadata`. Compare those values with SHA-256 hashes of your files.
If you manage the proxy with CloudFormation, make configuration changes in your template.
For more information, see [Bootstrap configuration](https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/how-envoy-runs.html#how-envoy-runs-bootstrap) and [Update a proxy configuration](https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/update-proxy-configuration.html) in the *Elastic Load Balancing for Envoy User Guide*.
*Required*: No
*Type*: [ConfigurationFile](aws-properties-elasticloadbalancingproxy-proxy-configurationfile.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomerKmsKeyArn`  <a name="cfn-elasticloadbalancingproxy-proxy-customerkmskeyarn"></a>
The ARN of a customer managed AWS Key Management Service (AWS KMS) key that encrypts the proxy's configuration file and configuration archive. If you don't specify a key, Elastic Load Balancing for Envoy uses an AWS owned key.
The key must be a symmetric encryption key that is enabled and in the same AWS account and Region as the proxy. Specify the full key ARN. The key policy must allow the principal that creates or updates the proxy to use `kms:DescribeKey`, `kms:GenerateDataKey`, and `kms:Decrypt`. It must also allow the `elasticloadbalancing.amazonaws.com` service principal to decrypt the configuration so that Elastic Load Balancing for Envoy can deliver it to the proxy.
You can add, change, or remove the key without replacing the proxy. To change the key, specify a different key ARN. To stop using a customer managed key, remove this property. Elastic Load Balancing for Envoy then encrypts the configuration with an AWS owned key. When you change or remove the key, the configuration file and configuration archive are re-encrypted with the new key or the AWS owned key, and the change is applied to the proxy in the same way as a configuration update. Keep the previous key enabled until the stack update completes, because a rollback re-encrypts the configuration with it.
If your template specifies `CustomerKmsKeyArn` and you change the key outside CloudFormation, for example with the `UpdateProxyConfiguration` operation, drift detection reports the change. A stack update restores your template's key only when your template's `ConfigurationFile`, `ConfigurationArchive`, or `CustomerKmsKeyArn` changes. If your template doesn't specify a key, drift detection doesn't report a key added outside CloudFormation, and stack updates leave it in place.
For more information, see [Encrypt a proxy configuration with a customer managed key](https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/proxy-encryption.html) in the *Elastic Load Balancing for Envoy User Guide*.
*Required*: No
*Type*: String
*Pattern*: `^arn:[a-z-]+:kms:[a-z0-9-]+:[0-9]{12}:key/(mrk-)?[a-f0-9-]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpAddressingConfiguration`  <a name="cfn-elasticloadbalancingproxy-proxy-ipaddressingconfiguration"></a>
The IP addressing configuration of the proxy. This configuration determines how clients can reach the proxy and which DNS records the service publishes.
The IPv4 and IPv6 addressability settings can't both be `off`, and you can't combine `internal` for one protocol with `internet-facing` for the other. You can't change this configuration after you create the proxy.
For more information, see [IP address types](https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/how-proxies-work.html#how-proxies-work-ip-address-types) in the *Elastic Load Balancing for Envoy User Guide*.
*Required*: Yes
*Type*: [IpAddressingConfiguration](aws-properties-elasticloadbalancingproxy-proxy-ipaddressingconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-elasticloadbalancingproxy-proxy-name"></a>
The name of the proxy. The name must be unique within your AWS account for the Region. The name can have 1–32 characters. Valid characters are a-z, A-Z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character. The name can't start with `internal-`, in any combination of uppercase and lowercase letters.
*Required*: Yes
*Type*: String
*Pattern*: `(^[a-zA-Z0-9]+$|^[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]$)`
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProxyVersion`  <a name="cfn-elasticloadbalancingproxy-proxy-proxyversion"></a>
The Envoy version that the proxy runs, in `major.minor` format (for example, `1.40`). To get the versions that you can specify, call the [ListProxyVersions](https://docs.aws.amazon.com/elasticloadbalancing/elb-proxy/latest/APIReference/API_ListProxyVersions.html) operation. Within a version, Elastic Load Balancing for Envoy applies Envoy patch releases and operating system updates for you.
For more information, see [Envoy versions](https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/how-envoy-runs.html#how-envoy-runs-versions) in the *Elastic Load Balancing for Envoy User Guide*.
*Required*: Yes
*Type*: String
*Pattern*: `^\d+\.\d+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-elasticloadbalancingproxy-proxy-rolearn"></a>
The ARN of the proxy role, an IAM role that Elastic Load Balancing for Envoy assumes for the proxy. The role's trust policy must allow the `elasticloadbalancing.amazonaws.com` service principal to call `sts:AssumeRole`. Don't add an `aws:SourceAccount` condition to the trust policy. If you do, the create fails with "Unable to assume role" because Elastic Load Balancing for Envoy can't assume the role. The role must be in the same AWS account as the proxy and can't be a service-linked role.
Elastic Load Balancing for Envoy uses the role to publish Envoy logs to Amazon CloudWatch Logs. At a minimum, the role must allow `logs:CreateLogGroup`, `logs:CreateLogStream`, and `logs:PutLogEvents` on log groups under `/aws/elb-proxy/`. The role also provides the permissions that the code your Envoy configuration runs, such as filters and extensions, needs when it calls AWS services. You need `iam:PassRole` permission for this role.
For more information, see [Create a proxy role](https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/setting-up.html#setting-up-proxy-role) in the *Elastic Load Balancing for Envoy User Guide*.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z-]+:iam::[0-9]{12}:role/.+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityGroups`  <a name="cfn-elasticloadbalancingproxy-proxy-securitygroups"></a>
The IDs of the security groups for the proxy. Specify at least one security group. Each security group ID can have 1–1024 characters. The number of security groups and their combined rules must be within your Amazon VPC quotas for security groups per network interface. Security group rules control the traffic that can reach the proxy and the traffic that the proxy can send. All security groups must belong to the proxy's VPC. You can update the security groups without replacing the proxy.
If you change the proxy's security groups outside CloudFormation, for example with the `UpdateProxyNetworkConfiguration` operation, drift detection reports the change. A stack update doesn't restore your template's security groups unless your template's `SecurityGroups` or `Subnets` changes.
For more information, see [Security groups](https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/how-proxies-work.html#how-proxies-work-security-groups) and [Update proxy network settings](https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/update-network-settings.html) in the *Elastic Load Balancing for Envoy User Guide*.
*Required*: Yes
*Type*: Array of String
*Maximum*: `1024`
*Minimum*: `1 | 1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subnets`  <a name="cfn-elasticloadbalancingproxy-proxy-subnets"></a>
The IDs of the subnets that the proxy is deployed into. Specify at least two subnets, each in a different Availability Zone, and all in the same VPC. The subnets must be in Availability Zones, not in Local Zones, Wavelength Zones, or Outposts. Each subnet ID can have 1–1024 characters.
If IPv6 addressability isn't `off`, each subnet must have an associated IPv6 CIDR block. If IPv4 addressability is `off`, the subnets must be IPv6-only subnets. Otherwise, the subnets can't be IPv6-only subnets.
You can update the subnets after you create the proxy, but all subnets must remain in the proxy's original VPC. You can't move a proxy to another VPC.
If you change the proxy's subnets outside CloudFormation, for example with the `UpdateProxyNetworkConfiguration` operation, drift detection reports the change. A stack update doesn't restore your template's subnets unless your template's `SecurityGroups` or `Subnets` changes. Subnets and security groups are updated together; see the `SecurityGroups` property.
For more information, see [Update proxy network settings](https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/update-network-settings.html) in the *Elastic Load Balancing for Envoy User Guide*.
*Required*: Yes
*Type*: Array of String
*Maximum*: `1024`
*Minimum*: `1 | 1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-elasticloadbalancingproxy-proxy-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-elasticloadbalancingproxy-proxy-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-elasticloadbalancingproxy-proxy-type"></a>
The type of the proxy. The only supported value is `envoy`.
*Required*: Yes
*Type*: String
*Allowed values*: `envoy`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-elasticloadbalancingproxy-proxy-return-values"></a>

### Ref
<a name="aws-resource-elasticloadbalancingproxy-proxy-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the proxy, such as `arn:aws:elasticloadbalancing:us-east-1:123456789012:proxy/my-proxy:0123456789abcdef`.

For more information, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-elasticloadbalancingproxy-proxy-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-elasticloadbalancingproxy-proxy-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the proxy.

`AvailabilityZones`  <a name="AvailabilityZones-fn::getatt"></a>
The subnets that the proxy is deployed into, together with their Availability Zones.

`ConfigurationMetadata.ConfigArchiveHash`  <a name="ConfigurationMetadata.ConfigArchiveHash-fn::getatt"></a>
The SHA-256 hash of the configuration archive, as a lowercase hexadecimal string. This value is absent when the proxy has no configuration archive.

`ConfigurationMetadata.ConfigArchiveLastUpdatedAt`  <a name="ConfigurationMetadata.ConfigArchiveLastUpdatedAt-fn::getatt"></a>
The date and time when the configuration archive was last updated. This value is absent when the proxy has no configuration archive.

`ConfigurationMetadata.ConfigFileHash`  <a name="ConfigurationMetadata.ConfigFileHash-fn::getatt"></a>
The SHA-256 hash of the configuration file, as a lowercase hexadecimal string.

`ConfigurationMetadata.ConfigFileLastUpdatedAt`  <a name="ConfigurationMetadata.ConfigFileLastUpdatedAt-fn::getatt"></a>
The date and time when the configuration file was last updated.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time when the proxy was created.

`DnsName`  <a name="DnsName-fn::getatt"></a>
The DNS name of the proxy. Clients use this name to send traffic to the proxy.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the proxy. Valid values are the following:
+ `create-in-progress` – The proxy is being created.
+ `active` – The proxy is fully provisioned and serving traffic.
+ `action-required` – The proxy might be impaired and requires action from you. To see the reasons, call the [GetProxy](https://docs.aws.amazon.com/elasticloadbalancing/elb-proxy/latest/APIReference/API_GetProxy.html) operation and check `status.reasons`.
+ `create-failed` – The proxy failed to create.
+ `delete-in-progress` – The proxy is being deleted.
+ `update-in-progress` – The proxy's Envoy version is being updated.
+ `cancel-update-in-progress` – A version update is being canceled.
When CloudFormation finishes creating the proxy, the proxy has the status `active`. If the proxy enters `create-failed` or `action-required` during creation, CloudFormation fails the create and includes the status reasons in the error message.
The create can also time out. If the proxy doesn't become `active` within 1 hour and doesn't report a failure, CloudFormation fails the create with the message "Exceeded attempts to wait for stabilization." This can happen when an Availability Zone can't provision capacity. CloudFormation then rolls back and deletes the proxy. You can retry the create later.

`VpcId`  <a name="VpcId-fn::getatt"></a>
The ID of the VPC that contains the proxy. The service derives this value from the subnets that you specify.

## Examples
<a name="aws-resource-elasticloadbalancingproxy-proxy--examples"></a>

**Topics**
+ [Example - Create a proxy](#aws-resource-elasticloadbalancingproxy-proxy--examples--Example_-_Create_a_proxy)
+ [Example - Associate an AWS WAF web ACL with a proxy](#aws-resource-elasticloadbalancingproxy-proxy--examples--Example_-_Associate_an_WAF_web_ACL_with_a_proxy)

### Example - Create a proxy
<a name="aws-resource-elasticloadbalancingproxy-proxy--examples--Example_-_Create_a_proxy"></a>

The following example creates an internal, IPv4-only proxy that runs Envoy 1.40 and responds to HTTP requests on port 80 with a fixed message. The Envoy configuration is written inline and encoded with `Fn::Base64`. Specify an existing proxy role, at least two subnets in different Availability Zones, and a security group as parameters.

#### JSON
<a name="aws-resource-elasticloadbalancingproxy-proxy--examples--Example_-_Create_a_proxy--json"></a>

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Parameters": {
    "ProxyRoleArn": {
      "Type": "String",
      "Description": "ARN of the proxy role"
    },
    "SubnetIds": {
      "Type": "List<AWS::EC2::Subnet::Id>",
      "Description": "At least two subnets in different Availability Zones of the same VPC"
    },
    "SecurityGroupId": {
      "Type": "AWS::EC2::SecurityGroup::Id",
      "Description": "Security group for the proxy"
    }
  },
  "Resources": {
    "Proxy": {
      "Type": "AWS::ElasticLoadBalancingProxy::Proxy",
      "Properties": {
        "Name": "my-proxy",
        "Type": "envoy",
        "ProxyVersion": "1.40",
        "RoleArn": {
          "Ref": "ProxyRoleArn"
        },
        "IpAddressingConfiguration": {
          "Ipv4Addressability": "internal",
          "Ipv6Addressability": "off"
        },
        "Subnets": {
          "Ref": "SubnetIds"
        },
        "SecurityGroups": [
          {
            "Ref": "SecurityGroupId"
          }
        ],
        "ConfigurationFile": {
          "ConfigurationBytes": {
            "Fn::Base64": "admin:\n  address:\n    socket_address:\n      address: 127.0.0.1\n      port_value: 9901\n\nstatic_resources:\n  listeners:\n  - name: listener_0\n    address:\n      socket_address:\n        address: 0.0.0.0\n        port_value: 80\n    filter_chains:\n    - filters:\n      - name: envoy.filters.network.http_connection_manager\n        typed_config:\n          \"@type\": type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager\n          stat_prefix: ingress_http\n          route_config:\n            name: local_route\n            virtual_hosts:\n            - name: local_service\n              domains: [\"*\"]\n              routes:\n              - match:\n                  prefix: \"/\"\n                direct_response:\n                  status: 200\n                  body:\n                    inline_string: \"Hello from ELB for Envoy\\n\"\n          http_filters:\n          - name: envoy.filters.http.router\n            typed_config:\n              \"@type\": type.googleapis.com/envoy.extensions.filters.http.router.v3.Router\n"
          }
        },
        "Attributes": [
          {
            "Key": "envoy.log_level",
            "Value": "info"
          }
        ],
        "Tags": [
          {
            "Key": "environment",
            "Value": "test"
          }
        ]
      }
    }
  },
  "Outputs": {
    "ProxyDnsName": {
      "Value": {
        "Fn::GetAtt": [
          "Proxy",
          "DnsName"
        ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-elasticloadbalancingproxy-proxy--examples--Example_-_Create_a_proxy--yaml"></a>

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Parameters:
  ProxyRoleArn:
    Type: String
    Description: ARN of the proxy role
  SubnetIds:
    Type: List<AWS::EC2::Subnet::Id>
    Description: At least two subnets in different Availability Zones of the same VPC
  SecurityGroupId:
    Type: AWS::EC2::SecurityGroup::Id
    Description: Security group for the proxy
Resources:
  Proxy:
    Type: AWS::ElasticLoadBalancingProxy::Proxy
    Properties:
      Name: my-proxy
      Type: envoy
      ProxyVersion: '1.40'
      RoleArn:
        Ref: ProxyRoleArn
      IpAddressingConfiguration:
        Ipv4Addressability: internal
        Ipv6Addressability: 'off'
      Subnets:
        Ref: SubnetIds
      SecurityGroups:
        - Ref: SecurityGroupId
      ConfigurationFile:
        ConfigurationBytes:
          Fn::Base64: |
            admin:
              address:
                socket_address:
                  address: 127.0.0.1
                  port_value: 9901

            static_resources:
              listeners:
              - name: listener_0
                address:
                  socket_address:
                    address: 0.0.0.0
                    port_value: 80
                filter_chains:
                - filters:
                  - name: envoy.filters.network.http_connection_manager
                    typed_config:
                      "@type": type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager
                      stat_prefix: ingress_http
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
                                inline_string: "Hello from ELB for Envoy\n"
                      http_filters:
                      - name: envoy.filters.http.router
                        typed_config:
                          "@type": type.googleapis.com/envoy.extensions.filters.http.router.v3.Router
      Attributes:
        - Key: envoy.log_level
          Value: info
      Tags:
        - Key: environment
          Value: test
Outputs:
  ProxyDnsName:
    Value:
      Fn::GetAtt: [Proxy, DnsName]
```

### Example - Associate an AWS WAF web ACL with a proxy
<a name="aws-resource-elasticloadbalancingproxy-proxy--examples--Example_-_Associate_an_WAF_web_ACL_with_a_proxy"></a>

The following example creates a proxy, a regional AWS WAF web ACL, and an `AWS::WAFv2::WebACLAssociation` that associates the web ACL with the proxy. To change the web ACL, update `WebACLArn` on the association. To remove it, delete the `AWS::WAFv2::WebACLAssociation` resource. The parameters are the same as in the first example.

#### JSON
<a name="aws-resource-elasticloadbalancingproxy-proxy--examples--Example_-_Associate_an_WAF_web_ACL_with_a_proxy--json"></a>

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Parameters": {
    "ProxyRoleArn": {
      "Type": "String",
      "Description": "ARN of the proxy role"
    },
    "SubnetIds": {
      "Type": "List<AWS::EC2::Subnet::Id>",
      "Description": "At least two subnets in different Availability Zones of the same VPC"
    },
    "SecurityGroupId": {
      "Type": "AWS::EC2::SecurityGroup::Id",
      "Description": "Security group for the proxy"
    }
  },
  "Resources": {
    "Proxy": {
      "Type": "AWS::ElasticLoadBalancingProxy::Proxy",
      "Properties": {
        "Name": "my-proxy",
        "Type": "envoy",
        "ProxyVersion": "1.40",
        "RoleArn": {
          "Ref": "ProxyRoleArn"
        },
        "IpAddressingConfiguration": {
          "Ipv4Addressability": "internal",
          "Ipv6Addressability": "off"
        },
        "Subnets": {
          "Ref": "SubnetIds"
        },
        "SecurityGroups": [
          {
            "Ref": "SecurityGroupId"
          }
        ],
        "ConfigurationFile": {
          "ConfigurationBytes": {
            "Fn::Base64": "admin:\n  address:\n    socket_address:\n      address: 127.0.0.1\n      port_value: 9901\n\nstatic_resources:\n  listeners:\n  - name: listener_0\n    address:\n      socket_address:\n        address: 0.0.0.0\n        port_value: 80\n    filter_chains:\n    - filters:\n      - name: envoy.filters.network.http_connection_manager\n        typed_config:\n          \"@type\": type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager\n          stat_prefix: ingress_http\n          route_config:\n            name: local_route\n            virtual_hosts:\n            - name: local_service\n              domains: [\"*\"]\n              routes:\n              - match:\n                  prefix: \"/\"\n                direct_response:\n                  status: 200\n                  body:\n                    inline_string: \"Hello from ELB for Envoy\\n\"\n          http_filters:\n          - name: envoy.filters.http.router\n            typed_config:\n              \"@type\": type.googleapis.com/envoy.extensions.filters.http.router.v3.Router\n"
          }
        }
      }
    },
    "WebACL": {
      "Type": "AWS::WAFv2::WebACL",
      "Properties": {
        "Name": "my-proxy-web-acl",
        "Scope": "REGIONAL",
        "DefaultAction": {
          "Allow": {}
        },
        "VisibilityConfig": {
          "SampledRequestsEnabled": true,
          "CloudWatchMetricsEnabled": true,
          "MetricName": "my-proxy-web-acl"
        }
      }
    },
    "WebACLAssociation": {
      "Type": "AWS::WAFv2::WebACLAssociation",
      "Properties": {
        "ResourceArn": {
          "Ref": "Proxy"
        },
        "WebACLArn": {
          "Fn::GetAtt": [
            "WebACL",
            "Arn"
          ]
        }
      }
    }
  },
  "Outputs": {
    "ProxyDnsName": {
      "Value": {
        "Fn::GetAtt": [
          "Proxy",
          "DnsName"
        ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-elasticloadbalancingproxy-proxy--examples--Example_-_Associate_an_WAF_web_ACL_with_a_proxy--yaml"></a>

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Parameters:
  ProxyRoleArn:
    Type: String
    Description: ARN of the proxy role
  SubnetIds:
    Type: List<AWS::EC2::Subnet::Id>
    Description: At least two subnets in different Availability Zones of the same VPC
  SecurityGroupId:
    Type: AWS::EC2::SecurityGroup::Id
    Description: Security group for the proxy
Resources:
  Proxy:
    Type: AWS::ElasticLoadBalancingProxy::Proxy
    Properties:
      Name: my-proxy
      Type: envoy
      ProxyVersion: '1.40'
      RoleArn:
        Ref: ProxyRoleArn
      IpAddressingConfiguration:
        Ipv4Addressability: internal
        Ipv6Addressability: 'off'
      Subnets:
        Ref: SubnetIds
      SecurityGroups:
        - Ref: SecurityGroupId
      ConfigurationFile:
        ConfigurationBytes:
          Fn::Base64: |
            admin:
              address:
                socket_address:
                  address: 127.0.0.1
                  port_value: 9901

            static_resources:
              listeners:
              - name: listener_0
                address:
                  socket_address:
                    address: 0.0.0.0
                    port_value: 80
                filter_chains:
                - filters:
                  - name: envoy.filters.network.http_connection_manager
                    typed_config:
                      "@type": type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager
                      stat_prefix: ingress_http
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
                                inline_string: "Hello from ELB for Envoy\n"
                      http_filters:
                      - name: envoy.filters.http.router
                        typed_config:
                          "@type": type.googleapis.com/envoy.extensions.filters.http.router.v3.Router
  WebACL:
    Type: AWS::WAFv2::WebACL
    Properties:
      Name: my-proxy-web-acl
      Scope: REGIONAL
      DefaultAction:
        Allow: {}
      VisibilityConfig:
        SampledRequestsEnabled: true
        CloudWatchMetricsEnabled: true
        MetricName: my-proxy-web-acl
  WebACLAssociation:
    Type: AWS::WAFv2::WebACLAssociation
    Properties:
      ResourceArn:
        Ref: Proxy
      WebACLArn:
        Fn::GetAtt: [WebACL, Arn]
Outputs:
  ProxyDnsName:
    Value:
      Fn::GetAtt: [Proxy, DnsName]
```

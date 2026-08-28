---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-kerberosattributes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Cluster KerberosAttributes
<a name="aws-properties-emr-cluster-kerberosattributes"></a>

`KerberosAttributes` is a property of the `AWS::EMR::Cluster` resource. `KerberosAttributes` define the cluster-specific Kerberos configuration when Kerberos authentication is enabled using a security configuration. The cluster-specific configuration must be compatible with the security configuration. For more information see [Use Kerberos Authentication](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-kerberos.html) in the *EMR Management Guide*.

## Syntax
<a name="aws-properties-emr-cluster-kerberosattributes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-cluster-kerberosattributes-syntax.json"></a>

```
{
  "[ADDomainJoinPassword](#cfn-emr-cluster-kerberosattributes-addomainjoinpassword)" : {{String}},
  "[ADDomainJoinUser](#cfn-emr-cluster-kerberosattributes-addomainjoinuser)" : {{String}},
  "[CrossRealmTrustPrincipalPassword](#cfn-emr-cluster-kerberosattributes-crossrealmtrustprincipalpassword)" : {{String}},
  "[KdcAdminPassword](#cfn-emr-cluster-kerberosattributes-kdcadminpassword)" : {{String}},
  "[Realm](#cfn-emr-cluster-kerberosattributes-realm)" : {{String}}
}
```

### YAML
<a name="aws-properties-emr-cluster-kerberosattributes-syntax.yaml"></a>

```
  [ADDomainJoinPassword](#cfn-emr-cluster-kerberosattributes-addomainjoinpassword): {{String}}
  [ADDomainJoinUser](#cfn-emr-cluster-kerberosattributes-addomainjoinuser): {{String}}
  [CrossRealmTrustPrincipalPassword](#cfn-emr-cluster-kerberosattributes-crossrealmtrustprincipalpassword): {{String}}
  [KdcAdminPassword](#cfn-emr-cluster-kerberosattributes-kdcadminpassword): {{String}}
  [Realm](#cfn-emr-cluster-kerberosattributes-realm): {{String}}
```

## Properties
<a name="aws-properties-emr-cluster-kerberosattributes-properties"></a>

`ADDomainJoinPassword`  <a name="cfn-emr-cluster-kerberosattributes-addomainjoinpassword"></a>
The Active Directory password for `ADDomainJoinUser`.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ADDomainJoinUser`  <a name="cfn-emr-cluster-kerberosattributes-addomainjoinuser"></a>
Required only when establishing a cross-realm trust with an Active Directory domain. A user with sufficient privileges to join resources to the domain.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CrossRealmTrustPrincipalPassword`  <a name="cfn-emr-cluster-kerberosattributes-crossrealmtrustprincipalpassword"></a>
Required only when establishing a cross-realm trust with a KDC in a different realm. The cross-realm principal password, which must be identical across realms.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KdcAdminPassword`  <a name="cfn-emr-cluster-kerberosattributes-kdcadminpassword"></a>
The password used within the cluster for the kadmin service on the cluster-dedicated KDC, which maintains Kerberos principals, password policies, and keytabs for the cluster.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Realm`  <a name="cfn-emr-cluster-kerberosattributes-realm"></a>
The name of the Kerberos realm to which all nodes in a cluster belong. For example, `EC2.INTERNAL`.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

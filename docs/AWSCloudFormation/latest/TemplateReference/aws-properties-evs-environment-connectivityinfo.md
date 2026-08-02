---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-evs-environment-connectivityinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EVS::Environment ConnectivityInfo
<a name="aws-properties-evs-environment-connectivityinfo"></a>

The connectivity configuration for the environment. Amazon EVS requires that you specify two route server peer IDs. During environment creation, the route server endpoints peer with the NSX uplink VLAN for connectivity to the NSX overlay network.

**Note**
Not supported when `vcfVersion` is `SELF_DEPLOYED`.

## Syntax
<a name="aws-properties-evs-environment-connectivityinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-evs-environment-connectivityinfo-syntax.json"></a>

```
{
  "[PrivateRouteServerPeerings](#cfn-evs-environment-connectivityinfo-privaterouteserverpeerings)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-evs-environment-connectivityinfo-syntax.yaml"></a>

```
  [PrivateRouteServerPeerings](#cfn-evs-environment-connectivityinfo-privaterouteserverpeerings): {{
    - String}}
```

## Properties
<a name="aws-properties-evs-environment-connectivityinfo-properties"></a>

`PrivateRouteServerPeerings`  <a name="cfn-evs-environment-connectivityinfo-privaterouteserverpeerings"></a>
The unique IDs for private route server peers.
*Required*: Yes
*Type*: Array of String
*Minimum*: `2`
*Maximum*: `2`
*Update requires*: Updates are not supported.

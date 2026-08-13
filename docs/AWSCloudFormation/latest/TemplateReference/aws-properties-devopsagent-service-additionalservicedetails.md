---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-additionalservicedetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service AdditionalServiceDetails
<a name="aws-properties-devopsagent-service-additionalservicedetails"></a>

Additional details specific to the service type, returned after registration.

## Syntax
<a name="aws-properties-devopsagent-service-additionalservicedetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-additionalservicedetails-syntax.json"></a>

```
{
  "[AzureIdentity](#cfn-devopsagent-service-additionalservicedetails-azureidentity)" : {{RegisteredAzureIdentityDetails}},
  "[Dynatrace](#cfn-devopsagent-service-additionalservicedetails-dynatrace)" : {{RegisteredDynatraceDetails}},
  "[GitLab](#cfn-devopsagent-service-additionalservicedetails-gitlab)" : {{RegisteredGitLabServiceDetails}},
  "[MCPServer](#cfn-devopsagent-service-additionalservicedetails-mcpserver)" : {{RegisteredMCPServerDetails}},
  "[MCPServerGrafana](#cfn-devopsagent-service-additionalservicedetails-mcpservergrafana)" : {{RegisteredMCPServerGrafanaDetails}},
  "[MCPServerNewRelic](#cfn-devopsagent-service-additionalservicedetails-mcpservernewrelic)" : {{RegisteredNewRelicDetails}},
  "[MCPServerSigV4](#cfn-devopsagent-service-additionalservicedetails-mcpserversigv4)" : {{RegisteredMCPServerSigV4Details}},
  "[MCPServerSplunk](#cfn-devopsagent-service-additionalservicedetails-mcpserversplunk)" : {{RegisteredMCPServerDetails}},
  "[PagerDuty](#cfn-devopsagent-service-additionalservicedetails-pagerduty)" : {{RegisteredPagerDutyDetails}},
  "[ServiceNow](#cfn-devopsagent-service-additionalservicedetails-servicenow)" : {{RegisteredServiceNowDetails}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-additionalservicedetails-syntax.yaml"></a>

```
  [AzureIdentity](#cfn-devopsagent-service-additionalservicedetails-azureidentity): {{
    RegisteredAzureIdentityDetails}}
  [Dynatrace](#cfn-devopsagent-service-additionalservicedetails-dynatrace): {{
    RegisteredDynatraceDetails}}
  [GitLab](#cfn-devopsagent-service-additionalservicedetails-gitlab): {{
    RegisteredGitLabServiceDetails}}
  [MCPServer](#cfn-devopsagent-service-additionalservicedetails-mcpserver): {{
    RegisteredMCPServerDetails}}
  [MCPServerGrafana](#cfn-devopsagent-service-additionalservicedetails-mcpservergrafana): {{
    RegisteredMCPServerGrafanaDetails}}
  [MCPServerNewRelic](#cfn-devopsagent-service-additionalservicedetails-mcpservernewrelic): {{
    RegisteredNewRelicDetails}}
  [MCPServerSigV4](#cfn-devopsagent-service-additionalservicedetails-mcpserversigv4): {{
    RegisteredMCPServerSigV4Details}}
  [MCPServerSplunk](#cfn-devopsagent-service-additionalservicedetails-mcpserversplunk): {{
    RegisteredMCPServerDetails}}
  [PagerDuty](#cfn-devopsagent-service-additionalservicedetails-pagerduty): {{
    RegisteredPagerDutyDetails}}
  [ServiceNow](#cfn-devopsagent-service-additionalservicedetails-servicenow): {{
    RegisteredServiceNowDetails}}
```

## Properties
<a name="aws-properties-devopsagent-service-additionalservicedetails-properties"></a>

`AzureIdentity`  <a name="cfn-devopsagent-service-additionalservicedetails-azureidentity"></a>
Azure identity service details returned after registration.
*Required*: No
*Type*: [RegisteredAzureIdentityDetails](aws-properties-devopsagent-service-registeredazureidentitydetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Dynatrace`  <a name="cfn-devopsagent-service-additionalservicedetails-dynatrace"></a>
Dynatrace service details returned after registration.
*Required*: No
*Type*: [RegisteredDynatraceDetails](aws-properties-devopsagent-service-registereddynatracedetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GitLab`  <a name="cfn-devopsagent-service-additionalservicedetails-gitlab"></a>
GitLab service details returned after registration.
*Required*: No
*Type*: [RegisteredGitLabServiceDetails](aws-properties-devopsagent-service-registeredgitlabservicedetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MCPServer`  <a name="cfn-devopsagent-service-additionalservicedetails-mcpserver"></a>
Custom MCP server details returned after registration.
*Required*: No
*Type*: [RegisteredMCPServerDetails](aws-properties-devopsagent-service-registeredmcpserverdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MCPServerGrafana`  <a name="cfn-devopsagent-service-additionalservicedetails-mcpservergrafana"></a>
Grafana MCP server details returned after registration.
*Required*: No
*Type*: [RegisteredMCPServerGrafanaDetails](aws-properties-devopsagent-service-registeredmcpservergrafanadetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MCPServerNewRelic`  <a name="cfn-devopsagent-service-additionalservicedetails-mcpservernewrelic"></a>
New Relic MCP server details returned after registration.
*Required*: No
*Type*: [RegisteredNewRelicDetails](aws-properties-devopsagent-service-registerednewrelicdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MCPServerSigV4`  <a name="cfn-devopsagent-service-additionalservicedetails-mcpserversigv4"></a>
SigV4-authenticated MCP server details returned after registration.
*Required*: No
*Type*: [RegisteredMCPServerSigV4Details](aws-properties-devopsagent-service-registeredmcpserversigv4details.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MCPServerSplunk`  <a name="cfn-devopsagent-service-additionalservicedetails-mcpserversplunk"></a>
Splunk MCP server details returned after registration.
*Required*: No
*Type*: [RegisteredMCPServerDetails](aws-properties-devopsagent-service-registeredmcpserverdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PagerDuty`  <a name="cfn-devopsagent-service-additionalservicedetails-pagerduty"></a>
PagerDuty service details returned after registration.
*Required*: No
*Type*: [RegisteredPagerDutyDetails](aws-properties-devopsagent-service-registeredpagerdutydetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceNow`  <a name="cfn-devopsagent-service-additionalservicedetails-servicenow"></a>
ServiceNow service details returned after registration.
*Required*: No
*Type*: [RegisteredServiceNowDetails](aws-properties-devopsagent-service-registeredservicenowdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

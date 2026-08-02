---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/troubleshooting.html
---

# Troubleshooting
<a name="troubleshooting"></a>

This section provides troubleshooting information for Spatial Data Management on AWS.

## Retrieve deployment information
<a name="retrieve-deployment-information"></a>

If you need to retrieve deployment information such as the portal URL or API endpoint, you can use the AWS CLI to query AWS CloudFormation outputs.

### Retrieve portal URL
<a name="retrieve-portal-url"></a>

To retrieve the portal URL from your deployment:

```
aws cloudformation describe-stacks --stack-name $(aws cloudformation list-stack-resources --stack-name <YOUR STACK> --query 'StackResourceSummaries[?starts_with(LogicalResourceId, `PortalStackNested`)].PhysicalResourceId' --output text) --query 'Stacks[0].Outputs[?OutputKey==`PortalCloudFrontDistributionUrl`].OutputValue' --output text
```

Replace `<YOUR STACK>` with your CloudFormation stack name (for example, `SpatialDataManagement`).

### Retrieve API endpoint
<a name="retrieve-api-endpoint"></a>

To retrieve the API endpoint from your deployment:

```
aws cloudformation describe-stacks --stack-name $(aws cloudformation list-stack-resources --stack-name <YOUR STACK> --query 'StackResourceSummaries[?starts_with(LogicalResourceId, `AssetManagementStackNestedStack`)].PhysicalResourceId' --output text) --query 'Stacks[0].Outputs[?OutputKey==`ApiUrl`].OutputValue' --output text
```

Replace `<YOUR STACK>` with your CloudFormation stack name (for example, `SpatialDataManagement`).

### Verify authentication status
<a name="verify-authentication-status"></a>

To verify your CLI authentication status and confirm API availability:

```
spatial-data-mgmt auth status
```

Example output:

```
Profile Name: demo-environment
Source: PORTAL_DESKTOP_LOGIN
Status: AUTHENTICATED
API Availability: True
```

If the status shows `AUTHENTICATED` and `API Availability: True`, your CLI is properly configured and connected to the API.

### Verify project access
<a name="verify-project-access"></a>

To check if you have any projects assigned or created by you, use the following command. This is helpful if you suspect the application has an issue and projects are not showing in the interface:

```
spatial-data-mgmt project list
```

This command returns a list of projects you have access to along with their attributes, including project ID, name, description, and your permission level.

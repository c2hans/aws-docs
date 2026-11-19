---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-dx-telemetry-sharing-with-wan-service-providers/operational-runbook.html
---

# Operational Runbook

This section provides partition-independent operational commands for deploying, validating, and revoking the framework.

## Deploy the Framework
<a name="deploy-the-framework.3ca4bd9c-35ce-50d8-8810-509df1392a15"></a>

```
# Detect partition, account, and region
AWS_PARTITION=$(aws sts get-caller-identity --query 'Arn' --output text | cut -d: -f2)
ACCOUNT_ID=$(aws sts get-caller-identity --query 'Account' --output text)
REGION=$(aws configure get region)

# Generate ExternalId
EXTERNAL_ID=$(uuidgen)

# Deploy CloudFormation stack
aws cloudformation deploy \
  --template-file iac/cloudformation/dx-info-sharing.yaml \
  --stack-name dx-info-sharing \
  --parameter-overrides \
    ESPAccountId=<ACCOUNT_NUMBER> \
    ExternalId=$EXTERNAL_ID \
  --capabilities CAPABILITY_NAMED_IAM

# Retrieve outputs
aws cloudformation describe-stacks \
  --stack-name dx-info-sharing \
  --query 'Stacks[0].Outputs' --output table

# Tag DX resources (partition-independent ARN)
aws directconnect tag-resource \
  --resource-arn arn:${AWS_PARTITION}:directconnect:${REGION}:${ACCOUNT_ID}:dxcon/dxcon-xxx \
  --tags key=DXInfoSharing,value=enabled \
         key=AccountPOC,value=owner@customer.com \
         key=TechnicalPOC,value=netadmin@customer.com \
         key=NOCContact,value=noc@customer.com \
         key=Criticality,value=MissionEssential
```

## Validate Deployment
<a name="validate-deployment.25e1fa6f-3b7b-5417-a716-835aa8317eeb"></a>

```
# Verify IAM role
aws iam get-role --role-name DXNetworkOperatorRole
aws iam list-attached-role-policies --role-name DXNetworkOperatorRole

# Verify governance rules (only if Config governance was deployed separately)
aws configservice describe-config-rules --output table \
  --query "ConfigRules[?contains(ConfigRuleName, 'dx-info-sharing')]"
```

### Role Assumption Validation — ExternalId Enforcement Modes
<a name="role-assumption-validation---externalid-enforcement-modes.645a41bb-c320-5d06-b144-a816ba5a7d13"></a>

The following commands are executed from the WSP/ESP account. Replace CUSTOMER\_ACCOUNT\_ID with the customer account ID hosting the DXNetworkOperatorRole.

**Note**
*This example uses jq to parse JSON output. If jq is not available, equivalent AWS CLI --query expressions may be used.*

When ExternalId enforcement is enabled (CLI/SDK only; Console Switch Role will fail):

```
AWS_PARTITION=$(aws sts get-caller-identity --query 'Arn' --output text | cut -d: -f2)
CUSTOMER_ACCOUNT_ID=<customer-account-id>
ROLE_ARN=arn:${AWS_PARTITION}:iam::${CUSTOMER_ACCOUNT_ID}:role/DXNetworkOperatorRole

CREDS=$(aws sts assume-role \
  --role-arn $ROLE_ARN \
  --role-session-name dx-validation \
  --external-id <ExternalId> \
  --query 'Credentials' --output json)

export AWS_ACCESS_KEY_ID=$(echo $CREDS | jq -r '.AccessKeyId')
export AWS_SECRET_ACCESS_KEY=$(echo $CREDS | jq -r '.SecretAccessKey')
export AWS_SESSION_TOKEN=$(echo $CREDS | jq -r '.SessionToken')
```

When ExternalId enforcement is removed (CLI/SDK and Console Switch Role both supported):

```
AWS_PARTITION=$(aws sts get-caller-identity --query 'Arn' --output text | cut -d: -f2)
CUSTOMER_ACCOUNT_ID=<customer-account-id>
ROLE_ARN=arn:${AWS_PARTITION}:iam::${CUSTOMER_ACCOUNT_ID}:role/DXNetworkOperatorRole

CREDS=$(aws sts assume-role \
  --role-arn $ROLE_ARN \
  --role-session-name dx-validation \
  --query 'Credentials' --output json)

export AWS_ACCESS_KEY_ID=$(echo $CREDS | jq -r '.AccessKeyId')
export AWS_SECRET_ACCESS_KEY=$(echo $CREDS | jq -r '.SecretAccessKey')
export AWS_SESSION_TOKEN=$(echo $CREDS | jq -r '.SessionToken')
```

After assuming the role using either mode, validate read access:

```
# Validate DX read access
aws directconnect describe-connections --max-results 5

# Validate CloudWatch read access (query scoped to AWS/DX)
aws cloudwatch list-metrics --namespace AWS/DX --max-items 5
```

This confirms that the role can retrieve Direct Connect configuration and metrics as expected. Execute governance validation only if AWS Config or alternative compliance mechanisms were deployed separately.

## Revocation Procedures
<a name="revocation-procedures.77fb29c4-61f9-5f0f-8749-d970dc8ea6a1"></a>

This section provides partition-independent operational commands for each revocation level. Operators should execute only the levels appropriate to the situation, proceeding from least to most disruptive.

```
# Detect partition, account, and region
AWS_PARTITION=$(aws sts get-caller-identity --query 'Arn' --output text | cut -d: -f2)
ACCOUNT_ID=$(aws sts get-caller-identity --query 'Account' --output text)
REGION=$(aws configure get region)
```

### Scope Reduction
<a name="scope-reduction.4d1c9683-468c-5ab5-8416-2640d0946893"></a>

Remove sharing tags from Direct Connect resources. The WSP/ESP can still assume the role and query describe APIs and CloudWatch metrics, but tag:GetResources returns no operational metadata. Does not invalidate issued STS credentials.

```
# Remove sharing tags from DX resources
aws directconnect untag-resource \
  --resource-arn arn:${AWS_PARTITION}:directconnect:${REGION}:${ACCOUNT_ID}:dxcon/dxcon-xxx \
  --tag-keys DXInfoSharing AccountPOC TechnicalPOC NOCContact Criticality
```

### Session Revocation
<a name="session-revocation.25ed2c55-7955-5d59-80d6-8aba5f464a4b"></a>

Invalidate all in-flight STS credentials. This is AWS's primary documented mechanism for immediate credential revocation. It attaches the AWSRevokeOlderSessions inline policy, which uses the aws:TokenIssueTime condition key to deny all permissions to credentials issued before the specified timestamp. New sessions assumed after the revocation remain functional. Takes effect within seconds.

```
# Invalidate all in-flight credentials
REVOCATION_DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

aws iam put-role-policy \
  --role-name DXNetworkOperatorRole \
  --policy-name AWSRevokeOlderSessions \
  --policy-document "{
    \"Version\": \"2012-10-17\",
    \"Statement\": [{
      \"Effect\": \"Deny\",
      \"Action\": [\"*\"],
      \"Resource\": [\"*\"],
      \"Condition\": {
        \"DateLessThan\": {
          \"aws:TokenIssueTime\": \"${REVOCATION_DATE}\"
        }
      }
    }]
  }"
```

### Role Disablement
<a name="role-disablement.ad91896f-1a23-585b-b1c7-a6abdf69d27b"></a>

Prevent new role assumptions while preserving the role for potential re-enablement. Modify the trust policy to deny all principals. Does not invalidate already-issued credentials; combine with session revocation for complete effect. AWS documents this as the recommended approach for disabling a role without deleting it.

```
# Prevent new role assumptions by modifying trust policy
aws iam update-assume-role-policy \
  --role-name DXNetworkOperatorRole \
  --policy-document "{
    \"Version\": \"2012-10-17\",
    \"Statement\": [{
      \"Sid\": \"DenyAll\",
      \"Effect\": \"Deny\",
      \"Principal\": {\"AWS\": \"*\"},
      \"Action\": \"sts:AssumeRole\"
    }]
  }"

# Verify disablement
aws iam get-role --role-name DXNetworkOperatorRole \
  --query 'Role.AssumeRolePolicyDocument' --output json
```

### Role Deletion
<a name="role-deletion.b0842388-8300-57f6-b510-d5fef5caa5e1"></a>

Permanent removal. Appropriate only when the trust relationship is permanently ended. AWS recommends considering disablement before deletion. Requires redeployment of the CloudFormation stack to restore.

```
# Remove inline revocation policy (if attached)
aws iam delete-role-policy --role-name DXNetworkOperatorRole \
  --policy-name AWSRevokeOlderSessions

# Detach managed policy
aws iam detach-role-policy --role-name DXNetworkOperatorRole \
  --policy-arn arn:${AWS_PARTITION}:iam::${ACCOUNT_ID}:policy/DXNetworkOperatorPolicy

# Delete role
aws iam delete-role --role-name DXNetworkOperatorRole

# Verify deletion
aws iam get-role --role-name DXNetworkOperatorRole
# Expected: NoSuchEntity error
```

After role deletion, review CloudTrail logs for unauthorized activity during the 90 days preceding termination, follow organizational incident response procedures, and determine whether to redeploy the framework.

---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/route-calls-events-cli.html
---

# Routing calls to AWS Lambda functions for Amazon Chime SDK PSTN audio (AWS CLI)
<a name="route-calls-events-cli"></a>

This tutorial guides you through the process of setting up call routing to Lambda functions using Amazon Chime SDK PSTN audio service. You'll learn how to create Lambda functions, set up SIP media applications, and configure SIP rules to handle incoming calls.

## Prerequisites
<a name="route-calls-events-cli-prerequisites"></a>

Before you begin this tutorial, make sure you do the following:
+ Install the AWS CLI. For more information, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS CLI User Guide*.
+ Configure your AWS CLI with appropriate credentials. Run `aws configure` if you haven't set up your credentials yet.
+ Have basic familiarity with AWS Lambda and Amazon Chime SDK concepts.
+ Set up sufficient permissions to create and manage Amazon Chime SDK and Lambda resources in your AWS account.
+ For the phone number-based routing, you need to have a phone number in your Amazon Chime SDK phone number inventory.
+ For the Voice Connector-based routing, you need to have a Voice Connector configured in your account.

## Cost considerations
<a name="route-calls-events-cli-cost"></a>

The tutorial includes cleanup instructions to ensure you don't incur ongoing charges after completion. For more information, see [Amazon Chime SDK Pricing](https://aws.amazon.com/chime/chime-sdk/pricing/).

Let's get started with setting up call routing for Amazon Chime SDK PSTN audio.

## Search for and provision phone numbers
<a name="route-calls-events-cli-search-provision"></a>

Before creating SIP rules with phone number triggers, you need to have phone numbers in your Amazon Chime SDK inventory. Here's how to search for available phone numbers and provision them.

**Example : Search for available phone numbers**

```
# Search for available toll-free phone numbers
aws chime-sdk-voice search-available-phone-numbers \
  --phone-number-type TollFree \
  --country US \
  --toll-free-prefix 844 \
  --max-results 5 \
  --region us-east-1
```

This command searches for available toll-free phone numbers with the prefix 844 in the US. You can modify the parameters to search for different types of numbers.

**Example : Provision a phone number**
After you find an available phone number, you can provision it using the following command:

```
# Order a phone number
aws chime-sdk-voice create-phone-number-order \
  --product-type SipMediaApplicationDialIn \
  --e164-phone-numbers "{{+18445550100}}" \
  --region us-east-1
```

Replace `+18445550100` with an actual available phone number from your search results. This command will provision the phone number to your account.

**Example : Check phone number status**
After ordering a phone number, you can check its status:

```
# Get the phone number order status
aws chime-sdk-voice get-phone-number-order \
  --phone-number-order-id abcd1234-5678-90ab-cdef-EXAMPLE55555 \
  --region us-east-1
```

Replace the order ID with the one returned from the `create-phone-number-order` command.

**Example : List phone numbers in your inventory**
To see all phone numbers in your inventory:

```
# List all phone numbers
aws chime-sdk-voice list-phone-numbers \
  --region us-east-1
```
To find unassigned phone numbers that can be used for SIP rules:

```
# List unassigned phone numbers
aws chime-sdk-voice list-phone-numbers \
  --region us-east-1 \
  --query "PhoneNumbers[?Status=='Unassigned'].E164PhoneNumber"
```

## Create a Lambda function for call handling
<a name="route-calls-events-cli-create-function"></a>

Now, let's create a Lambda function that will handle incoming calls. The function will receive events from the PSTN audio service and respond with instructions on how to handle the call.

**Example : Create an IAM role for Lambda**
Before creating the Lambda function, you need to create an IAM role that grants the necessary permissions.

```
cat > lambda-trust-policy.json << EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
```

```
aws iam create-role --role-name ChimeSDKLambdaRole \
  --assume-role-policy-document file://lambda-trust-policy.json
```

```
aws iam attach-role-policy --role-name ChimeSDKLambdaRole \
  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```
These commands create an IAM role that allows Lambda to assume it and attach the basic execution policy, which provides permissions for Lambda to write logs to CloudWatch.

**Example : Create a Lambda function**
Now, create a simple Lambda function that will handle incoming calls.

```
mkdir -p lambda
cat > lambda/index.js << EOF
exports.handler = async (event) => {
  console.log('Received event:', JSON.stringify(event, null, 2));

  // Simple call handling logic
  const response = {
    SchemaVersion: '1.0',
    Actions: [
      {
        Type: 'Speak',
        Parameters: {
          Engine: 'neural',
          Text: 'Hello! This is a test call from Amazon Chime SDK PSTN Audio.',
          VoiceId: 'Joanna'
        }
      },
      {
        Type: 'Hangup',
        Parameters: {
          SipResponseCode: '200'
        }
      }
    ]
  };

  return response;
};
EOF
```

```
cd lambda
zip -r function.zip index.js
cd ..
```

```
# Get your AWS account ID
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

aws lambda create-function \
  --function-name ChimeSDKCallHandler \
  --runtime nodejs18.x \
  --role arn:aws:iam::${ACCOUNT_ID}:role/ChimeSDKLambdaRole \
  --handler index.handler \
  --zip-file fileb://lambda/function.zip
```
This Lambda function responds to incoming calls with a spoken message and then hangs up.

**Example : Add Lambda permission for Amazon Chime SDK**
Grant permission to the Amazon Chime SDK service to invoke your Lambda function.

```
# Get your AWS account ID
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

aws lambda add-permission \
  --function-name ChimeSDKCallHandler \
  --statement-id ChimeSDK \
  --action lambda:InvokeFunction \
  --principal voiceconnector.chime.amazonaws.com \
  --source-account ${ACCOUNT_ID}
```
This command allows the Amazon Chime SDK Voice Connector service to invoke your Lambda function.

## Create a SIP media application
<a name="route-calls-events-cli-create-sip-app"></a>

SIP media applications connect your Lambda function to the PSTN audio service. In this section, you'll create a SIP media application that uses your Lambda function.

**Example : Create the SIP media application**

```
# Get your Lambda function ARN
LAMBDA_ARN=$(aws lambda get-function --function-name ChimeSDKCallHandler --query Configuration.FunctionArn --output text)

aws chime-sdk-voice create-sip-media-application \
  --aws-region us-east-1 \
  --name "MyCallHandlerApp" \
  --endpoints "[{\"LambdaArn\":\"${LAMBDA_ARN}\"}]"
```
The SIP media application acts as a bridge between the PSTN audio service and your Lambda function.

**Example : Get the SIP media application ID**
After creating the SIP media application, you need to retrieve its ID for use later in the tutorial.

```
SIP_MEDIA_APP_ID=$(aws chime-sdk-voice list-sip-media-applications \
  --query "SipMediaApplications[?Name=='MyCallHandlerApp'].SipMediaApplicationId" \
  --output text)

echo "SIP Media Application ID: ${SIP_MEDIA_APP_ID}"
```
Make note of the SIP media application ID returned by this command, as you'll need it when creating SIP rules.

## Set up call routing with SIP rules
<a name="route-calls-events-cli-call-routing-sip-rules"></a>

SIP rules determine how incoming calls are routed to your SIP media applications. You can create rules based on phone numbers or Voice Connector hostnames.

**Example : Create a SIP rule with phone number trigger**
To route calls based on a phone number, use the following command:

```
# Get an unassigned phone number from your inventory
PHONE_NUMBER=$(aws chime-sdk-voice list-phone-numbers \
  --query "PhoneNumbers[?Status=='Unassigned'].E164PhoneNumber | [0]" \
  --output text)

# If no unassigned phone number is found, you'll need to provision one
if [ -z "$PHONE_NUMBER" ] || [ "$PHONE_NUMBER" == "None" ]; then
  echo "No unassigned phone numbers found. Please provision a phone number first."
  exit 1
fi

echo "Using phone number: ${PHONE_NUMBER}"

aws chime-sdk-voice create-sip-rule \
  --name "IncomingCallRule" \
  --trigger-type ToPhoneNumber \
  --trigger-value "${PHONE_NUMBER}" \
  --target-applications "[{\"SipMediaApplicationId\":\"${SIP_MEDIA_APP_ID}\",\"Priority\":1}]"
```
This command creates a SIP rule that routes calls to your phone number to your SIP media application.

**Example : Create a SIP rule with Request URI hostname trigger**
Alternatively, you can route calls based on the request URI of an incoming Voice Connector SIP call:

```
# Replace with your Voice Connector hostname
VOICE_CONNECTOR_HOST="{{example}}.voiceconnector.chime.aws"

aws chime-sdk-voice create-sip-rule \
  --name "VoiceConnectorRule" \
  --trigger-type RequestUriHostname \
  --trigger-value "${VOICE_CONNECTOR_HOST}" \
  --target-applications "[{\"SipMediaApplicationId\":\"${SIP_MEDIA_APP_ID}\",\"Priority\":1}]"
```
Replace the hostname with your Voice Connector's outbound hostname.

## Set up redundancy with multiple SIP media applications
<a name="route-calls-events-cli-sip-redundancy"></a>

For redundancy and failover, you can create multiple SIP media applications in the same AWS Region and specify their order of priority.

**Example : Create a backup Lambda function**
First, create a backup Lambda function in the same Region.

```
cat > lambda/backup-index.js >< EOF
exports.handler = async (event) => {
  console.log('Received event in backup handler:', JSON.stringify(event, null, 2));

  // Simple call handling logic for backup
  const response = {
    SchemaVersion: '1.0',
    Actions: [
      {
        Type: 'Speak',
        Parameters: {
          Engine: 'neural',
          Text: 'Hello! This is the backup handler for Amazon Chime SDK PSTN Audio.',
          VoiceId: 'Matthew'
        }
      },
      {
        Type: 'Hangup',
        Parameters: {
          SipResponseCode: '200'
        }
      }
    ]
  };

  return response;
};
EOF
```

```
                    cd lambda
                    zip -r backup-function.zip backup-index.js
                    cd ..
```

```
                    # Get your AWS account ID
                    ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

                    aws lambda create-function \
                    --function-name ChimeSDKBackupHandler \
                    --runtime nodejs18.x \
                    --role arn:aws:iam::${ACCOUNT_ID}:role/ChimeSDKLambdaRole \
                    --handler backup-index.handler \
                    --zip-file fileb://lambda/backup-function.zip
```

**Example : Add Lambda permission for Amazon Chime SDK to the backup function**

```
                    # Get your AWS account ID
                    ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

                    aws lambda add-permission \
                    --function-name ChimeSDKBackupHandler \
                    --statement-id ChimeSDK \
                    --action lambda:InvokeFunction \
                    --principal voiceconnector.chime.amazonaws.com \
                    --source-account ${ACCOUNT_ID}
```

**Example : Create a backup SIP media application**

```
# Get your backup Lambda function ARN
BACKUP_LAMBDA_ARN=$(aws lambda get-function --function-name ChimeSDKBackupHandler --query Configuration.FunctionArn --output text)

aws chime-sdk-voice create-sip-media-application \
  --aws-region us-east-1 \
  --name "BackupCallHandlerApp" \
  --endpoints "[{\"LambdaArn\":\"${BACKUP_LAMBDA_ARN}\"}]"

# Get the backup SIP media application ID
BACKUP_SIP_MEDIA_APP_ID=$(aws chime-sdk-voice list-sip-media-applications \
  --query "SipMediaApplications[?Name=='BackupCallHandlerApp'].SipMediaApplicationId" \
  --output text)
```

**Example : Get the SIP rule ID**

```
SIP_RULE_ID=$(aws chime-sdk-voice list-sip-rules \
  --query "SipRules[?Name=='IncomingCallRule'].SipRuleId" \
  --output text)
```

**Example : Update SIP rule to include both applications with priorities**

```
aws chime-sdk-voice update-sip-rule \
  --sip-rule-id ${SIP_RULE_ID} \
  --target-applications "[{\"SipMediaApplicationId\":\"${SIP_MEDIA_APP_ID}\",\"Priority\":1},{\"SipMediaApplicationId\":\"${BACKUP_SIP_MEDIA_APP_ID}\",\"Priority\":2}]"
```
This command updates the SIP rule to include both the primary and backup SIP media applications with their respective priorities.

## Create outbound calls
<a name="route-calls-events-cli-create-outbound"></a>

You can also create outbound calls that invoke your Lambda function using the `CreateSIPMediaApplicationCall` API.

```
# Use a phone number from your inventory for outbound calling
FROM_PHONE_NUMBER=${PHONE_NUMBER}
TO_PHONE_NUMBER="{{+12065550102}}"  # Replace with a valid destination number

aws chime-sdk-voice create-sip-media-application-call \
  --from-phone-number "${FROM_PHONE_NUMBER}" \
  --to-phone-number "${TO_PHONE_NUMBER}" \
  --sip-media-application-id ${SIP_MEDIA_APP_ID}
```

Replace the destination phone number with a valid number. You need to have the phone numbers in your inventory to make real calls.

## Trigger Lambda during an active call
<a name="route-calls-events-cli-trigger-lambda"></a>

You can trigger your Lambda function during an active call using the `UpdateSIPMediaApplicationCall` API.

```
# Replace with an actual transaction ID from an active call
TRANSACTION_ID="{{txn-3ac9de3f-6b5a-4be9-9e7e-EXAMPLE33333}}"

aws chime-sdk-voice update-sip-media-application-call \
  --sip-media-application-id ${SIP_MEDIA_APP_ID} \
  --transaction-id ${TRANSACTION_ID} \
  --arguments '{"action":"custom-action"}'
```

The transaction ID is provided in the event data sent to your Lambda function when a call is active.

## Clean up resources
<a name="route-calls-events-cli-cleanup-resources"></a>

When you're finished with this tutorial, you should delete the resources you created to avoid incurring additional charges.

**Example : Delete SIP rules**

```
# Get the SIP rule ID if you don't have it
SIP_RULE_ID=$(aws chime-sdk-voice list-sip-rules \
  --query "SipRules[?Name=='IncomingCallRule'].SipRuleId" \
  --output text)

aws chime-sdk-voice delete-sip-rule --sip-rule-id ${SIP_RULE_ID}
```

**Example : Delete SIP media applications**

```
# Get SIP media application IDs if you don't have them
SIP_MEDIA_APP_ID=$(aws chime-sdk-voice list-sip-media-applications \
  --query "SipMediaApplications[?Name=='MyCallHandlerApp'].SipMediaApplicationId" \
  --output text)

BACKUP_SIP_MEDIA_APP_ID=$(aws chime-sdk-voice list-sip-media-applications \
  --query "SipMediaApplications[?Name=='BackupCallHandlerApp'].SipMediaApplicationId" \
  --output text)

aws chime-sdk-voice delete-sip-media-application --sip-media-application-id ${SIP_MEDIA_APP_ID}
aws chime-sdk-voice delete-sip-media-application --sip-media-application-id ${BACKUP_SIP_MEDIA_APP_ID}
```

**Example : Delete Lambda functions**

```
aws lambda delete-function --function-name ChimeSDKCallHandler
aws lambda delete-function --function-name ChimeSDKBackupHandler
```

**Example : Delete IAM role**

```
aws iam detach-role-policy --role-name ChimeSDKLambdaRole \
  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

aws iam delete-role --role-name ChimeSDKLambdaRole
```

**Example : Release phone numbers**
If you no longer need the phone numbers, you can release them:

```
# List phone numbers
aws chime-sdk-voice list-phone-numbers

# Delete a specific phone number
aws chime-sdk-voice delete-phone-number --phone-number-id ${PHONE_NUMBER}
```

Note that phone numbers enter a "ReleaseInProgress" status for 7 days before being fully released. During this period, you can restore them using the `restore-phone-number` command if needed.

## Going to production
<a name="route-calls-events-cli-going-to-production"></a>

This tutorial demonstrates the basic functionality of routing calls to Lambda functions using Amazon Chime SDK PSTN audio. However, for production environments, you should consider the following best practices:

### Security considerations
<a name="route-calls-events-cli-security"></a>
+ Implement least privilege permissions. Create custom IAM policies that grant only the specific permissions needed by your Lambda functions.
+ Add source ARN conditions to Lambda permissions. Restrict which SIP media applications can invoke your Lambda functions.
+ Implement input validation. Add validation to your Lambda functions to ensure they only process valid events.
+ Consider VPC deployment. For enhanced security, deploy your Lambda functions within a VPC with appropriate security groups.
+ Encrypt sensitive data. Use AWS Key Management Service to encrypt any sensitive data used by your application.

### Architecture considerations
<a name="route-calls-events-cli-architecture"></a>
+ Implement monitoring and logging. Set up CloudWatch alarms and logs to monitor your application's health and performance.
+ Add error handling. Implement comprehensive error handling in your Lambda functions.
+ Consider scaling limits. Be aware of service quotas and request increases if needed for high call volumes.
+ Implement infrastructure as code. Use CloudFormation or the AWS CDK to deploy your infrastructure.
+ Set up CI/CD pipelines. Implement continuous integration and deployment for your Lambda functions.

For more information about building production-ready applications, refer to:
+ [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
+ [Best Practices for Security, Identity, & Compliance](https://aws.amazon.com/architecture/security-identity-compliance/)
+ [Serverless Application Lens](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html)

## Next steps
<a name="route-calls-events-cli-next-steps"></a>

Now that you've learned how to route calls to Lambda functions using Amazon Chime SDK PSTN audio, you can explore more advanced features:
+ Integrate with Amazon Lex to manage the dialog interaction for an intelligent-agent scenario. For more information, see [Creating an Amazon Lex V2 bot for Amazon Chime SDK messaging](create-lex-bot.md).
+ Set up voice analytics to gain insights from your calls. For more information, see [Generating insights from calls using call analytics for the Amazon Chime SDK](call-analytics.md).
+ Explore advanced call control actions to build sophisticated call flows. For more information, see [Using call analytics configurations for the Amazon Chime SDK](using-call-analytics-configurations.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/solutions/latest/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws/roles-and-permissions.html
---

# Roles and permissions
<a name="roles-and-permissions"></a>

 This guidance uses AWS CodeBuild, AWS CloudFormation, and AWS CodePipeline for Continuous Delivery (CD) and AWS Glue and Amazon Athena for scientific analysis using a genomics data lake. Review the following CodeBuild, AWS CloudFormation, CodePipeline, AWS Glue, and Amazon Athena permissions to ensure that you have the appropriate permissions activated.

## Code deployment pipeline permissions
<a name="code-deployment-pipeline-permissions"></a>

 Use IAM to manage access to AWS CodeBuild jobs, AWS CloudFormation stacks, and the AWS CodePipeline `code` pipeline. CodeBuild jobs and the CodePipeline `code` pipeline have their own IAM roles and IAM policies.

 The following code examples demonstrate the IAM roles and supporting IAM policies defined in the `GenomicsAnalysisPipe/pipe_cfn.yml` file; including `CodeBuildRole`, `CodePipelineRole`, `CloudFormationRole`, and `SourceEventRole`.

### CloudFormation role
<a name="cloudformation-role"></a>

 `CloudFormationRole` defines the permissions needed for AWS CloudFormation to provision IAM roles, S3 buckets, an Amazon SageMaker AI notebook instance, and AWS Glue resources. AWS CloudFormation uses the CloudFormation action type in the CodePipeline.

```
CloudFormationRole:
    Type: AWS::IAM::Role
    Properties:
      Path: /
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Action:
              - sts:AssumeRole
            Principal:
              Service:
                - cloudformation.amazonaws.com
      Policies:
        - PolicyName: CloudFormationRolePolicy
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - iam:CreateRole
                  - iam:DeleteRole
                  - iam:PutRolePolicy
                  - iam:GetRolePolicy
                  - iam:DeleteRolePolicy
                  - iam:AttachRolePolicy
                  - iam:DetachRolePolicy
                  - iam:UpdateAssumeRolePolicy
                  - iam:PassRole
                  - iam:GetRole
                Resource:
                  - !Sub arn:aws:iam::${AWS::AccountId}:role/${ResourcePrefix}*
              - Effect: Allow
                Action:
                  - glue:CreateJob
                  - glue:UpdateJob
                  - glue:DeleteJob
                  - glue:GetJob
                Resource: '*'
              - Effect: Allow
                Action:
                  - glue:CreateSecurityConfiguration
                  - glue:GetSecurityConfiguration
                  - glue:DeleteSecurityConfiguration
                Resource: '*'
              - Effect: Allow
                Action:
                  - glue:CreateWorkflow
                  - glue:DeleteWorkflow
                  - glue:UpdateWorkflow
                Resource: '*'
              - Effect: Allow
                Action:
                  - glue:GetDataCatalogEncryptionSettings
                  - glue:PutDataCatalogEncryptionSettings
                  - glue:DeleteDataCatalogEncryptionSettings
                Resource:
                  - !Sub arn:aws:glue:${AWS::Region}:${AWS::AccountId}:catalog
              - Effect: Allow
                Action:
                  - glue:CreateDatabase
                  - glue:UpdateDatabase
                  - glue:DeleteDatabase
                  - glue:GetDatabase
                  - glue:GetDatabases
                  - glue:GetCrawler
                  - glue:CreateCrawler
                  - glue:UpdateCrawler
                  - glue:DeleteCrawler
                  - glue:StopCrawler
                  - glue:StopTrigger
                  - glue:GetTrigger
                  - glue:CreateTrigger
                  - glue:DeleteTrigger
                  - glue:UpdateTrigger
                Resource:
                  - !Sub arn:aws:glue:${AWS::Region}:${AWS::AccountId}:catalog
                  - !Sub arn:aws:glue:${AWS::Region}:${AWS::AccountId}:database/${ResourcePrefixLowercase}
                  - !Sub arn:aws:glue:${AWS::Region}:${AWS::AccountId}:table/${ResourcePrefixLowercase}/*
                  - !Sub arn:aws:glue:${AWS::Region}:${AWS::AccountId}:userDefinedFunction/${ResourcePrefixLowercase}/*
                  - !Sub arn:aws:glue:${AWS::Region}:${AWS::AccountId}:crawler/${ResourcePrefixLowercase}*
                  - !Sub arn:aws:glue:${AWS::Region}:${AWS::AccountId}:trigger/${ResourcePrefixLowercase}*
              - Effect: Allow
                Action:
                  - glue:CreateTable
                  - glue:UpdateTable
                  - glue:DeleteTable
                  - glue:SearchTables
                  - glue:GetTable
                  - glue:GetTables
                  - glue:GetPartitions
                Resource:
                  - !Sub arn:aws:glue:${AWS::Region}:${AWS::AccountId}:catalog
                  - !Sub arn:aws:glue:${AWS::Region}:${AWS::AccountId}:database/${ResourcePrefixLowercase}
                  - !Sub arn:aws:glue:${AWS::Region}:${AWS::AccountId}:table/${ResourcePrefixLowercase}/*
              - Effect: Allow
                Action:
                  - lambda:CreateFunction
                  - lambda:DeleteFunction
                  - lambda:GetFunctionConfiguration
                  - lambda:GetFunction
                  - lambda:InvokeFunction
                  - lambda:ListTags
                  - lambda:TagResource
                  - lambda:UntagResource
                  - lambda:UpdateFunctionCode
                  - lambda:UpdateFunctionConfiguration
                Resource:
                  - !Sub arn:aws:lambda:${AWS::Region}:${AWS::AccountId}:function:${ResourcePrefix}*
              - Effect: Allow
                Action:
                  - lambda:PublishLayerVersion
                  - lambda:DeleteLayerVersion
                  - lambda:GetLayerVersion
                Resource:
                  - !Sub arn:aws:lambda:${AWS::Region}:${AWS::AccountId}:layer:OmicsApiModels
                  - !Sub arn:aws:lambda:${AWS::Region}:${AWS::AccountId}:layer:OmicsApiModels:*
              - Effect: Allow
                Action:
                  - athena:GetWorkGroup
                  - athena:CreateWorkGroup
                  - athena:DeleteWorkGroup
                Resource:
                  - !Sub arn:aws:athena:${AWS::Region}:${AWS::AccountId}:workgroup/${ResourcePrefixLowercase}-${AWS::Region}
              - Effect: Allow
                Action:
                  - kms:CreateKey
                  - kms:GenerateDataKey
                Resource: '*'
              - Effect: Allow
                Action:
                  - s3:CreateBucket
                  - s3:DeleteBucket
                  - s3:GetObject
                Resource:
                  - !Sub ${BuildBucket.Arn}
                  - !Sub ${BuildBucket.Arn}/*
                  - !Sub ${ResourcesBucket.Arn}
                  - !Sub ${ResourcesBucket.Arn}/*
              - Effect: Allow
                Action:
                  - s3:GetObject
                Resource:
                  - !Sub ${ResourcesBucket.Arn}/artifacts/*
                  - arn:aws:s3:::aws-genomics-static-us-east-1/*
              - Effect: Allow
                Action:
                  - sagemaker:CreateNotebookInstanceLifecycleConfig
                  - sagemaker:DescribeNotebookInstanceLifecycleConfig
                  - sagemaker:UpdateNotebookInstanceLifecycleConfig
                  - sagemaker:DeleteNotebookInstanceLifecycleConfig
                  - sagemaker:CreateNotebookInstance
                  - sagemaker:UpdateNotebookInstance
                  - sagemaker:StartNotebookInstance
                  - sagemaker:DescribeNotebookInstance
                  - sagemaker:DeleteNotebookInstance
                  - sagemaker:StopNotebookInstance
                Resource:
                  - !Sub arn:aws:sagemaker:${AWS::Region}:${AWS::AccountId}:notebook-instance-lifecycle-config/${ResourcePrefixLowercase}*
                  - !Sub arn:aws:sagemaker:${AWS::Region}:${AWS::AccountId}:notebook-instance/${ResourcePrefixLowercase}*
```

### CodeBuild role
<a name="codebuild-role"></a>

 `CodeBuildRole` defines the permissions needed for CodeBuild to run a code build job that copies the resources needed to Amazon S3 buckets and build custom scripts that support Amazon Omics resource creation using AWS CloudFormation. The CodeBuild job is run using the CodeBuild action type in the CodePipeline.

```
CodeBuildRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          - Action:
              - sts:AssumeRole
            Effect: Allow
            Principal:
              Service:
                - codebuild.amazonaws.com
      Path: /
      Policies:
        - PolicyName: CodeBuildAccess
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Resource:
                  - !Sub arn:aws:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/codebuild/${ResourcePrefix}*
                Action:
                  - logs:CreateLogGroup
                  - logs:CreateLogStream
                  - logs:PutLogEvents
              - Effect: Allow
                Action:
                  - s3:GetObject
                  - s3:GetObjectVersion
                  - s3:PutObject
                Resource:
                  - !Sub ${BuildBucket.Arn}/*
                  - !Sub ${ResourcesBucket.Arn}/*
              - Effect: Allow
                Action:
                  - s3:ListBucket
                Resource:
                  - !Sub ${ResourcesBucket.Arn}
                  - !Sub ${DataLakeBucket.Arn}
              - Effect: Allow
                Action:
                  - s3:PutObject
                  - s3:PutObjectAcl
                Resource:
                  - !Sub ${ResourcesBucket.Arn}
                  - !Sub ${ResourcesBucket.Arn}/*
                  - !Sub ${DataLakeBucket.Arn}
                  - !Sub ${DataLakeBucket.Arn}/*
```

### Source event role
<a name="source-event-role"></a>

 `SourceEventRole` defines the permissions needed for an Amazon CloudWatch event to initiate the deployment pipeline.

```
SourceEventRole:
    Type: AWS::IAM::Role
    DependsOn: CodePipeline
    Description: IAM role to allow Amazon CloudWatch Events to trigger AWS CodePipeline
      execution
    Properties:
      AssumeRolePolicyDocument:
        Statement:
          - Action: sts:AssumeRole
            Effect: Allow
            Principal:
              Service:
                - events.amazonaws.com
            Sid: 1
      Policies:
        - PolicyName: CloudWatchEventPolicy
          PolicyDocument:
            Statement:
              - Action:
                  - codepipeline:StartPipelineExecution
                Effect: Allow
                Resource:
                  - !Sub arn:aws:codepipeline:${AWS::Region}:${AWS::AccountId}:${CodePipeline}*
```

## AWS Glue and Amazon SageMaker AI notebook permissions
<a name="aws-glue-and-amazon-sagemaker-notebook-permissions"></a>

 Use IAM to manage access to the datasets and scripts in Amazon S3 using AWS Glue, and to define the permissions for your Amazon SageMaker AI Jupyter notebook instance. Adding new AWS Glue jobs and crawlers does not require any changes to the following roles or policies, as long as you add those resources with the `${Project}` prefix.

 The following code examples demonstrate the IAM roles and supporting IAM policies defined in the `GenomicsAnalysisCode/code_cfn.yml` and `GenomicsAnalysisCode/TCIA_etl.yml` files, including `JobRole`, `GlueJobRole`, `CrawlerRole`, and `RunbookRole`.

### Job role
<a name="job-role"></a>

 `JobRole` defines the permissions needed for AWS Glue to run Extract, Transform, and Load (ETL).

 This role must be updated to get or put objects in additional S3 buckets in your AWS account or S3 buckets in other accounts.

```
JobRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - glue.amazonaws.com
            Action:
              - sts:AssumeRole
      Path: /
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole
      Policies:
        - PolicyName: s3_access
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - athena:StartQueryExecution
                  - athena:GetQueryExecution
                  - athena:GetQueryResults
                Resource:
                  - !Sub arn:aws:athena:${AWS::Region}:${AWS::AccountId}*
              - Effect: Allow
                Action:
                  - s3:GetObject
                  - s3:ListBucket
                Resource:
                  - !Sub arn:aws:s3:::${ResourcesBucket}
                  - !Sub arn:aws:s3:::${ResourcesBucket}/*
              - Effect: Allow
                Action:
                  - s3:PutObject
                  - s3:GetObject
                  - s3:ListBucket
                  - s3:DeleteObject
                Resource:
                  - !Sub arn:aws:s3:::${DataLakeBucket}
                  - !Sub arn:aws:s3:::${DataLakeBucket}/*
        - PolicyName: kms_access
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - kms:GenerateDataKey
                  - kms:Decrypt
                  - kms:Encrypt
                Resource:
                  - !GetAtt DataCatalogEncryptionKey.Arn
```

### Glue job role
<a name="glue-job-role"></a>

 `GlueJobRole` defines the permissions needed for AWS Glue to run Extract, Transform, and Load (ETL). In addition, it defines the permissions needed to run an AWS Glue crawler on a dataset in an Amazon S3 bucket, infer the schema, and add or update a table in the AWS Glue data catalog.

 This role must be updated to `get` or `put` objects in additional S3 buckets in your AWS account or S3 buckets in other accounts.

```
GlueJobRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: "Allow"
            Principal:
              Service: "glue.amazonaws.com"
            Action: "sts:AssumeRole"
      Path: "/"
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole
      Policies:
        - PolicyName: athena_access
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - athena:StartQueryExecution
                  - athena:GetQueryExecution
                  - athena:GetQueryResults
                Resource:
                  - !Sub arn:aws:athena:${AWS::Region}:${AWS::AccountId}:workgroup/primary
        - PolicyName: kms_access
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - kms:GenerateDataKey
                  - kms:Decrypt
                  - kms:Encrypt
                Resource:
                  - !ImportValue
                      Fn::Sub: '${ResourcePrefix}-DataCatalogEncryptionKeyArn'
        - PolicyName: "CrawlerAccess"
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
              - Effect: "Allow"
                Action:
                  - s3:PutObject
                  - s3:GetObject
                  - s3:ListBucket
                  - s3:DeleteObject
                Resource:
                  - !Sub 'arn:aws:s3:::${DataLakeBucket}'
                  - !Sub 'arn:aws:s3:::${DataLakeBucket}/*'
```

### Runbook role
<a name="runbook-role"></a>

 `RunbookRole` provides the permissions needed for the Amazon SageMaker AI Jupyter notebook instance to access the AWS Glue data catalog and use Amazon Athena to run queries against the data lake.

```
RunbookRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - sagemaker.amazonaws.com
            Action:
              - sts:AssumeRole
      Path: /
      Policies:
        - PolicyName: logs_access
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - logs:CreateLogStream
                  - logs:DescribeLogStreams
                  - logs:CreateLogGroup
                  - logs:PutLogEvents
                Resource:
                  - !Sub arn:aws:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/sagemaker/*
                  - !Sub arn:aws:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/sagemaker/*:log-stream:aws-glue-*
        - PolicyName: s3_access
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - s3:ListBucket
                  - s3:GetBucketLocation
                Resource:
                  - !Sub arn:aws:s3:::${DataLakeBucket}
                  - !Sub arn:aws:s3:::${ResourcesBucket}
              - Effect: Allow
                Action:
                  - s3:GetObject
                  - s3:GetObjectAcl
                  - s3:PutObject
                  - s3:DeleteObject
                Resource:
                  - !Sub arn:aws:s3:::${DataLakeBucket}/*
              - Effect: Allow
                Action:
                  - s3:GetObject
                Resource:
                  - !Sub arn:aws:s3:::${ResourcesBucket}/*
        - PolicyName: glue_access
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - glue:StartCrawler
                  - glue:StartJobRun
                  - glue:StartTrigger
                Resource:
                  - !Sub arn:aws:glue:${AWS::Region}:${AWS::AccountId}:crawler/${ResourcePrefixLowercase}*
                  - !Sub arn:aws:glue:${AWS::Region}:${AWS::AccountId}:job/${ResourcePrefixLowercase}*
                  - !Sub arn:aws:glue:${AWS::Region}:${AWS::AccountId}:trigger/${ResourcePrefixLowercase}*
              - Effect: Allow
                Action:
                  - kms:GenerateDataKey
                  - kms:Decrypt
                  - kms:Encrypt
                Resource:
                  - !GetAtt DataCatalogEncryptionKey.Arn
        - PolicyName: glue_table_access
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - glue:GetDatabases
                Resource: '*'
              - Effect: Allow
                Action:
                  - glue:GetDatabase
                  - glue:CreateDatabase
                Resource:
                  - !Sub arn:aws:glue:${AWS::Region}:${AWS::AccountId}:database/default
              - Effect: Allow
                Action:
                  - glue:GetTable
                  - glue:GetTables
                  - glue:CreateTable
                  - glue:UpdateTable
                  - glue:GetDatabase
                  - glue:GetPartition
                  - glue:GetPartitions
                  - glue:GetDevEndpoint
                  - glue:GetDevEndpoints
                  - glue:UpdateDevEndpoint
                Resource:
                  - !Sub arn:aws:glue:${AWS::Region}:${AWS::AccountId}:catalog
                  - !Sub arn:aws:glue:${AWS::Region}:${AWS::AccountId}:database/${ResourcePrefixLowercase}
                  - !Sub arn:aws:glue:${AWS::Region}:${AWS::AccountId}:table/${ResourcePrefixLowercase}/*
                  - !Sub arn:aws:glue:${AWS::Region}:${AWS::AccountId}:devEndpoint/*
        - PolicyName: athena_access
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - athena:StartQueryExecution
                  - athena:GetQueryExecution
                  - athena:GetQueryResults
                Resource:
                  - !Sub arn:aws:athena:${AWS::Region}:${AWS::AccountId}:workgroup/primary
        - PolicyName: cfn_access
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - cloudformation:DescribeStacks
                Resource:
                  - !Sub arn:aws:cloudformation:${AWS::Region}:${AWS::AccountId}:stack/${ResourcePrefix}*
        - PolicyName: kms_access
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - kms:GenerateDataKey
                  - kms:Decrypt
                  - kms:Encrypt
                Resource:
                  - !GetAtt DataCatalogEncryptionKey.Arn
```

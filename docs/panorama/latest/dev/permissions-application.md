---
source_url: https://docs.aws.amazon.com/panorama/latest/dev/permissions-application.html
---

End of support notice: On May 31, 2026, AWS will end support for AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama resources. For more information, see [AWS Panorama end of support](https://docs.aws.amazon.com/panorama/latest/dev/panorama-end-of-support.html).

# Granting permissions to an application
<a name="permissions-application"></a>

You can create a role for your application to grant it permission to call AWS services. By default, applications do not have any permissions. You create an application role in IAM and assign it to an application during deployment. To grant your application only the permissions that it needs, create a role for it with permissions for specific API actions.

The [sample application](gettingstarted-sample.md) includes an CloudFormation template and script that create an application role. It is a [service role](permissions-services.md) that AWS Panorama can assume. This role grants permission for the application to call CloudWatch to upload metrics.

**Example [aws-panorama-sample.yml](https://github.com/awsdocs/aws-panorama-developer-guide/blob/main/sample-apps/aws-panorama-sample/aws-panorama-sample.yml) – Application role**

```
Resources:
  runtimeRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          -
            Effect: Allow
            Principal:
              Service:
                - panorama.amazonaws.com
            Action:
              - sts:AssumeRole
      Policies:
        - PolicyName: cloudwatch-putmetrics
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action: 'cloudwatch:PutMetricData'
                Resource: '*'
      Path: /service-role/
```

You can extend this script to grant permissions to other services, by specifying a list of API actions or patterns for the value of `Action`.

For more information on permissions in AWS Panorama, see [AWS Panorama permissions](panorama-permissions.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Panorama. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query panorama` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

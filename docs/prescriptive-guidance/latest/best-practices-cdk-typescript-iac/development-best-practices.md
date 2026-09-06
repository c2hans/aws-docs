---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-cdk-typescript-iac/development-best-practices.html
---

# Adopt a test-driven development approach
<a name="development-best-practices"></a>

We recommend that you follow a test-driven development (TDD) approach with the AWS CDK. TDD** **is a software development approach where you develop test cases to specify and validate your code. In simple terms, first you create test cases for each functionality and if the test fails, then you write the new code to pass the test and make the code simple and bug-free.

You can use TDD to write the test case first. This helps you validate the infrastructure with different design constraints in terms of enforcing security policy for the resources and following a unique naming convention for the project. The standard approach to testing AWS CDK applications is to use the AWS CDK [assertions](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.assertions-readme.html) module and popular test frameworks, such as [Jest](https://jestjs.io/) for TypeScript and JavaScript or [pytest](https://docs.pytest.org/en/6.2.x/) for Python. There are two categories of tests that you can write for your AWS CDK applications:
+ Use **fine-grained assertions **to test a specific aspect of the generated CloudFormation template, such as "this resource has this property with this value." These tests can detect regressions and are also useful when you're developing new features using TDD (write a test first, then make it pass by writing a correct implementation). Fine-grained assertions are the tests you'll write the most.
+ Use **snapshot tests **to test the synthesized CloudFormation template against a previously-stored baseline template. Snapshot tests make it possible to refactor freely, since you can be sure that the refactored code works exactly the same way as the original. If the changes were intentional, you can accept a new baseline for future tests. However, AWS CDK upgrades can also cause synthesized templates to change, so you can't rely only on snapshots to make sure your implementation is correct.

## Unit test
<a name="unit-test.18a648ae-4ad4-5a26-8c91-a9026e128c89"></a>

This guide focuses on unit test integration for TypeScript specifically. To enable testing, make sure that your `package.json` file has the following libraries: `@types/jest`, `jest`, and `ts-jest` in `devDependencies`. To add these packages, run the `cdk init lib --language=typescript` command. After you run the preceding command, you see the following structure.

![Unit test structure](http://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-cdk-typescript-iac/images/guide-img/b7d5d887-7172-4d47-9f1f-1cf7ae181482/images/ace1c1b1-d95b-410f-8b6a-8c30621aec40.png)

The following code is an example of a `package.json` file that's enabled with the Jest library.

```
{
  ...
  "scripts": {
    "build": "npm run lint && tsc",
    "watch": "tsc -w",
    "test": "jest",
  },
  "devDependencies": {
    ...
    "@types/jest": "27.5.2",
    "jest": "27.5.1",
    "ts-jest": "27.1.5",
    ...
  }
}
```

Under the **Test** folder, you can write the test case. The following example shows a test case for an AWS CodePipeline construct.

```
import { Stack } from 'aws-cdk-lib';
import { Template } from 'aws-cdk-lib/assertions';
import * as CodePipeline from 'aws-cdk-lib/aws-codepipeline';
import * as CodePipelineActions from 'aws-cdk-lib/aws-codepipeline-actions';
import { MyPipelineStack } from '../lib/my-pipeline-stack';
test('Pipeline Created with GitHub Source', () => {
  // ARRANGE
  const stack = new Stack();
  // ACT
  new MyPipelineStack(stack, 'MyTestStack');
  // ASSERT
  const template = Template.fromStack(stack);
  // Verify that the pipeline resource is created
  template.resourceCountIs('AWS::CodePipeline::Pipeline', 1);
  // Verify that the pipeline has the expected stages with GitHub source
  template.hasResourceProperties('AWS::CodePipeline::Pipeline', {
    Stages: [
      {
        Name: 'Source',
        Actions: [
          {
            Name: 'SourceAction',
            ActionTypeId: {
              Category: 'Source',
              Owner: 'ThirdParty',
              Provider: 'GitHub',
              Version: '1'
            },
            Configuration: {
              Owner: {
                'Fn::Join': [
                  '',
                  [
                    '{{resolve:secretsmanager:',
                    {
                      Ref: 'GitHubTokenSecret'
                    },
                    ':SecretString:owner}}'
                  ]
                ]
              },
              Repo: {
                'Fn::Join': [
                  '',
                  [
                    '{{resolve:secretsmanager:',
                    {
                      Ref: 'GitHubTokenSecret'
                    },
                    ':SecretString:repo}}'
                  ]
                ]
              },
              Branch: 'main',
              OAuthToken: {
                'Fn::Join': [
                  '',
                  [
                    '{{resolve:secretsmanager:',
                    {
                      Ref: 'GitHubTokenSecret'
                    },
                    ':SecretString:token}}'
                  ]
                ]
              }
            },
            OutputArtifacts: [
              {
                Name: 'SourceOutput'
              }
            ],
            RunOrder: 1
          }
        ]
      },
      {
        Name: 'Build',
        Actions: [
          {
            Name: 'BuildAction',
            ActionTypeId: {
              Category: 'Build',
              Owner: 'AWS',
              Provider: 'CodeBuild',
              Version: '1'
            },
            InputArtifacts: [
              {
                Name: 'SourceOutput'
              }
            ],
            OutputArtifacts: [
              {
                Name: 'BuildOutput'
              }
            ],
            RunOrder: 1
          }
        ]
      }
      // Add more stage checks as needed
    ]
  });
  // Verify that a GitHub token secret is created
  template.resourceCountIs('AWS::SecretsManager::Secret', 1);
});
);
```

To run a test, run the `npm run test` command in your project. The test returns the following results.

```
PASS  test/codepipeline-module.test.ts (5.972 s)
   Code Pipeline Created (97 ms)
Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
Snapshots:   0 total
Time:        6.142 s, estimated 9 s
```

For more information on test cases, see [Testing constructs](https://docs.aws.amazon.com/cdk/v2/guide/testing.html) in the *AWS CDK Developer Guide*.

## Integration test
<a name="integration-test"></a>

Integration tests for AWS CDK constructs can also be included by using an `integ-tests` module. An integration test should be defined as an AWS CDK application. There should be a one-to-one relationship between an integration test and an AWS CDK application. For more information, visit [integ-tests-alpha module](https://docs.aws.amazon.com/cdk/api/v2/docs/integ-tests-alpha-readme.html) in the *AWS CDK API Reference*.

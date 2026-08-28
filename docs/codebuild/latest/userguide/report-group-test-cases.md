---
source_url: https://docs.aws.amazon.com/codebuild/latest/userguide/report-group-test-cases.html
---

# Specify test files
<a name="report-group-test-cases"></a>

 You specify the test result files and their location for each report group in the `reports` section of your build project's buildspec file. For more information, see [Reports syntax in the buildspec file](build-spec-ref.md#reports-buildspec-file).

 The following is a sample `reports` section that specifies two report groups for a build project. One is specified with its ARN, the other with a name. The `files` section specifies the files that contain the test case results. The optional `base-directory` section specifies the directory where the test case files are located. The optional `discard-paths` section specifies whether paths to test result files uploaded to an Amazon S3 bucket are discarded.

```
reports:
  arn:aws:codebuild:your-region:your-aws-account-id:report-group/report-group-name-1: #surefire junit reports
    files:
      - '**/*'
    base-directory: 'surefire/target/surefire-reports'
    discard-paths: false

  sampleReportGroup: #Cucumber reports from json plugin
    files:
      - 'cucumber-json/target/cucumber-json-report.json'
    file-format: CUCUMBERJSON #Type of the report, defaults to JUNITXML
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

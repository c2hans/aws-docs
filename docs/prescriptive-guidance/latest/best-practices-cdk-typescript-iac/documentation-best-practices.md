---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-cdk-typescript-iac/documentation-best-practices.html
---

# Develop and refine documentation
<a name="documentation-best-practices"></a>

Documentation is critical to the success of your project. Not only does documentation explain how your code works but it also helps developers better understand the features and functionality of your applications. Developing and refining high-quality documentation can strengthen the software development process, maintain high-quality software, and help with knowledge transfer between developers.

There are two categories of documentation: documentation inside the code and supporting documentation about the code. Documentation inside the code is in the form of comments. Supporting documentation about the code can be README files and external documents. It's not uncommon for developers to think of documentation as overhead, as the code itself is easy to understand. This could be true for small projects, but documentation is crucial for large-scale projects where multiple teams are involved.

It's a best practice for the author of the code to write the documentation since they have a good understanding of its functionalities. Developers can struggle with the additional overhead of maintaining separate supporting documentation. To overcome this challenge, developers can add the comments in the code and those comments can be extracted automatically so every version of code and documentation will be in sync.

There are a variety of different tools to help developers extract comments from code and generate the documentation for it. This guide focuses on TypeDoc as the preferred tool for AWS CDK constructs.

## Why code documentation is required for AWS CDK constructs
<a name="why-code-documentation-is-required-for-9999999999999999cdk--constructs.783c474b-1f45-51c1-aa90-726488ec1389"></a>

AWS CDK common constructs are created by multiple teams in an organization and shared across different teams for consumption. Good documentation helps the consumers of the construct library easily integrate constructs and build their infrastructure with minimum effort. Keeping all documents in sync is a big task. We recommend that you maintain the document inside the code, which will be extracted using the TypeDoc library.

## Using TypeDoc with the AWS Construct Library
<a name="using-typedoc-with-the-9999999999999999aws--construct-library.7a96c569-e390-5100-9257-f7017f54aebc"></a>

TypeDoc is a document generator for TypeScript. You can use TypeDoc to read your TypeScript source files, parse the comments in those files, and then generate a static site that contains documentation for your code. The following code shows you how to integrate TypeDoc with the AWS Construct Library, and then add the following packages in your `package.json` file in `devDependencies`.

```
{

  "devDependencies": {

    "typedoc-plugin-markdown": "^3.11.7",
    "typescript": "~3.9.7"
  },

}
```

To add `typedoc.json` in the CDK library folder, use the following code.

```
{
    "$schema": "https://typedoc.org/schema.json",
    "entryPoints": ["./lib"],
}
```

To generate the README files, run the `npx typedoc` command in the root directory of the AWS CDK construct library project.

The following sample document is generated by TypeDoc.

![Sample TypeDoc document](http://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-cdk-typescript-iac/images/guide-img/b7d5d887-7172-4d47-9f1f-1cf7ae181482/images/3525b7c2-7570-4535-90cc-090d8040d9f6.png)

For more information about TypeDoc integration options, see [Doc Comments](https://typedoc.org/guides/doccomments/) in the TypeDoc documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

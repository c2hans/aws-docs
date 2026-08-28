---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mainframe-decomposition-aws-transform/faq.html
---

# FAQ
<a name="faq"></a>

## Which file types does AWS Transform support?
<a name="which-file-types-does-9999999999999999trn--support-.93c4e634-7480-540d-8c07-ed1cea314205"></a>

Supported file types include COBOL, JCL, and IBM Db2. For a full list, see the [AWS Transform documentation](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe.html#transform-app-mainframe-supported-files).

## How long does the decomposition process typically take?
<a name="how-long-does-the-decomposition-process-typically-take-.31223044-e4e2-59be-91c7-3e8fd6a9508e"></a>

The duration varies based on application complexity and size. AWS Transform accelerates the process significantly, but you should plan for multiple iterations and stakeholder reviews.

## What's the difference between decomposition and refactoring?
<a name="what9999999999999999apos-s-the-difference-between-decomposition-and-refactoring-.9ca770ed-ccbd-58a4-9030-5450400a363f"></a>

Decomposition focuses on breaking an application down into logical domains, whereas refactoring involves transforming and generating Java code for the different components in each domain or wave. AWS Transform assists with both processes.

## Can I modify the decomposition suggestions provided by AWS Transform?
<a name="can-i-modify-the-decomposition-suggestions-provided-by-9999999999999999trn--.fbe40450-38c4-598c-ba0c-1cbd5b126c3c"></a>

Yes, you can review and modify domain groupings and wave plans. AWS Transform is designed to be a collaborative tool that uses both AI suggestions and human expertise.

## Which scheduler types or files does the current decomposition process support?
<a name="which-scheduler-types-or-files-does-the-current-decomposition-process-support-.e56a6eae-540c-533d-ae7a-3a9fe4bc0704"></a>

The process supports CA Jobtrac, CA 7 Workload Automation, and BMC Control-M.

## Is it mandatory to select seeds to create a domain?
<a name="is-it-mandatory-to-select-seeds-to-create-a-domain-.e14d9c40-0954-54a5-865d-2fcb541761a5"></a>

Yes, seeds are critical inputs for defining and creating domains. You can select one or more components as seeds for a particular domain.

## Can I upload a JSON file as seed input?
<a name="can-i-upload-a-json-file-as-seed-input-.3c74ef8a-23f9-5032-bba5-4689c7ef173e"></a>

Yes, you can. A larger code base typically includes more seeds per domain. You can create an input seed file in JSON format and upload it in the decomposition process.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cicd-litmus/litmus-test-for-cicd-pipelines.html
---

# Litmus test for CI/CD pipelines
<a name="litmus-test-for-cicd-pipelines"></a>

In chemistry, litmus paper is a thin strip of paper treated with a special red or blue dye that is used to determine the acidity of a substance. An acid turns blue litmus paper red, a base turns red litmus paper blue, and neutral substances don't affect the paper's color at all.

The way litmus paper determines acidity is by measuring a substance's pH level. If a pH level is higher than 8, it's acidic; if it's below 5, it's basic; and if it's between 5 and 8, it's neutral. Similarly, the [CI/CD litmus test](https://litmus.devops.aws.dev/) helps you measure the CI/CD level of your pipeline.

**To test whether your pipeline is fully CI/CD**

1. Start with a score of 0.

1. Answer each of the following questions, and add 1 to your score for each time you answer *yes*:
   + Do our repositories each have exactly one main branch that is used to deploy to environments?
   + Do we commit code to the main branch frequently and avoid having long-running feature branches?
   + Does our pipeline have a single point of entry? In other words, does our pipeline pull the code from each repository exactly one time?
   + Do we have more than one deployment environment?
   + When the pipeline is not running, are our upper and lower environments generally in sync?
   + Do we run tests on code before deploying?
   + Do we run tests on an environment before promoting to the next environment?
   + Does our pipeline do a full rollback and exit after a failure?
   + Does our pipeline restart from the first step when recovering from a failure?
   + Do we follow the same process to fix bugs in production that we do to release features to production?
   + Do we use some form of infrastructure as code (IaC) templates to deploy code?

1. Answer each of the following questions, and add 1 to your score for each time you answer *no*:
   + Do we ever deploy directly into a deployment environment from branches other than the main branch?
   + Do we ever deploy directly from any branch to an upper or production environment?
   + Do we often find bugs in upper environments that were not present in lower environments?
   + Do we ever bypass lower environments during a deployment?
   + Do we wait until a scheduled release time to deploy to production?
   + Do we regularly make updates in the production environment's console?
   + Are there any manual deployment steps that must be done in the production environment's console in order to complete deployment?
   + Does more than one person have write access to the production environment?
   + Do more than five people have write access to the production environment?

1. Divide your score by 2. This is your pipeline's CI/CD score.

1. Compare your pipeline's CI/CD score to the following table to determine your pipeline's CI/CD level.

<table>
<tbody>
</tbody>
</table>

If you scored below 8, we recommend that you set a goal to move gradually toward the next level. When that goal is achieved, then product stakeholders should assess if and when a new goal should be set. The intention of this exercise is not necessarily to advocate for a change to your pipeline, but rather to bring awareness of what a fully CI/CD deployment process looks like and where your pipelines currently sit on that spectrum.

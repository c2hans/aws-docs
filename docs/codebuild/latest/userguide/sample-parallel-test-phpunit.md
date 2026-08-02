---
source_url: https://docs.aws.amazon.com/codebuild/latest/userguide/sample-parallel-test-phpunit.html
---

# Configure parallel tests with PHPUnit
<a name="sample-parallel-test-phpunit"></a>

The following is sample of a `buildspec.yml` that shows parallel test execution with PHPUnit on an Linux platform:

```
version: 0.2

batch:
   fast-fail: false
   build-fanout:
     parallelism: 5
     ignore-failure: false

phases:
   install:
     commands:
       - echo 'Install dependencies'
       - composer require --dev phpunit/phpunit
   pre_build:
     commands:
       - echo 'prebuild'
   build:
     commands:
       - echo 'Running phpunit Tests'
       - composer dump-autoload
       - |
         codebuild-tests-run \
          --test-command "./vendor/bin/phpunit --debug" \
          --files-search "codebuild-glob-search '**/tests/*Test.php'"
   post_build:
       commands:
         - echo 'Test execution completed'
```

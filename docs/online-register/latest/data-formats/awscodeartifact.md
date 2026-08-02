---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/awscodeartifact.html
---

# Data retrieval APIs for AWS CodeArtifact
<a name="awscodeartifact"></a>

AWS CodeArtifact provides the following APIs for data retrieval.

****

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="codeartifact-DescribeDomain"></a>[https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribeDomain.html](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribeDomain.html) | Return information about a domain | Read |
| <a name="codeartifact-DescribePackage"></a>[https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribePackage.html](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribePackage.html) | Retrieve information about a package | Read |
| <a name="codeartifact-DescribePackageGroup"></a>[https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribePackageGroup.html](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribePackageGroup.html) | Return detailed information about a package group | Read |
| <a name="codeartifact-DescribePackageVersion"></a>[https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribePackageVersion.html](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribePackageVersion.html) | Return information about a package version | Read |
| <a name="codeartifact-DescribeRepository"></a>[https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribeRepository.html](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribeRepository.html) | Return detailed information about a repository | Read |
| <a name="codeartifact-GetAssociatedPackageGroup"></a>[https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetAssociatedPackageGroup.html](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetAssociatedPackageGroup.html) | Return a package's associated package group | Read |
| <a name="codeartifact-GetAuthorizationToken"></a>[https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetAuthorizationToken.html](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetAuthorizationToken.html) | Generate a temporary authentication token for accessing repositories in a domain | Read |
| <a name="codeartifact-GetDomainPermissionsPolicy"></a>[https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetDomainPermissionsPolicy.html](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetDomainPermissionsPolicy.html) | Return a domain's resource policy | Read |
| <a name="codeartifact-GetPackageVersionAsset"></a>[https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetPackageVersionAsset.html](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetPackageVersionAsset.html) | Return an asset (or file) that is part of a package version | Read |
| <a name="codeartifact-GetPackageVersionReadme"></a>[https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetPackageVersionReadme.html](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetPackageVersionReadme.html) | Return a package version's readme file | Read |
| <a name="codeartifact-GetRepositoryEndpoint"></a>[https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetRepositoryEndpoint.html](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetRepositoryEndpoint.html) | Return an endpoint for a repository | Read |
| <a name="codeartifact-GetRepositoryPermissionsPolicy"></a>[https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetRepositoryPermissionsPolicy.html](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetRepositoryPermissionsPolicy.html) | Return a repository's resource policy | Read |
| <a name="codeartifact-ListAllowedRepositoriesForGroup"></a>[https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListRepositoriesInDomain.html](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListRepositoriesInDomain.html) | List the allowed repositories for a package group | List |
| <a name="codeartifact-ListAssociatedPackages"></a>[https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListAssociatedPackages.html](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListAssociatedPackages.html) | List the packages associated to a package group | List |
| <a name="codeartifact-ListDomains"></a>[https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListDomains.html](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListDomains.html) | List the domains in the current user's AWS account | List |
| <a name="codeartifact-ListPackageGroups"></a>[https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageGroups.html](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageGroups.html) | List the package groups in a domain | List |
| <a name="codeartifact-ListPackageVersionAssets"></a>[https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersionAssets.html](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersionAssets.html) | List a package version's assets | List |
| <a name="codeartifact-ListPackageVersionDependencies"></a>[https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersionDependencies.html](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersionDependencies.html) | List the direct dependencies of a package version | List |
| <a name="codeartifact-ListPackageVersions"></a>[https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html) | List a package's versions | List |
| <a name="codeartifact-ListPackages"></a>[https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackages.html](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackages.html) | List the packages in a repository | List |
| <a name="codeartifact-ListRepositories"></a>[https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListRepositories.html](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListRepositories.html) | List the repositories administered by the calling account | List |
| <a name="codeartifact-ListRepositoriesInDomain"></a>[https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListRepositoriesInDomain.html](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListRepositoriesInDomain.html) | List the repositories in a domain | List |
| <a name="codeartifact-ListSubPackageGroups"></a>[https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListSubPackageGroups.html](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListSubPackageGroups.html) | List the sub package groups for a parent package group | List |
| <a name="codeartifact-ListTagsForResource"></a>[https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListTagsForResource.html](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListTagsForResource.html) | List tags for a CodeArtifact resource | List |
| <a name="codeartifact-ReadFromRepository"></a>[https://docs.aws.amazon.com/codeartifact/latest/ug/repo-policies.html](https://docs.aws.amazon.com/codeartifact/latest/ug/repo-policies.html) | Return package assets and metadata from a repository endpoint | Read |

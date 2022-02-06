## Manage infrastructure

### Config structure

`./terraform/live` contains configuration files per environment and devided on partitions depending on region

`./terraform/live/shared` environment contains resources which shared across environments

`./terraform/modules` contains terraform modules

### Resources

These configs are managing:

* VPC and subnets
* VPC peering
* Security Groups
* ALB (public and internal)
* EC2 instances
* EC2 VPN instance

### For existing configuration

To apply changes to certain terragrunt config `cd` to `./terraform/live/dev/eu-central-1/<config>` and execute `terragrunt plan/apply/<whatever>` there

### For new environment

1. Copy config from existing environment
```
cd ./terraform/live/dev
rsync -am -c -r --progress --exclude '.terragrunt-cache' . ../<new_env>
```
2. If you want to create environment in another region then set corresponding directory name `./terraform/live/<new_env>/<region>`
3. Change values in `./terraform/live/<new_env>/environment.hcl` and `./terraform/live/<new_env>/<region>/partition.hcl`. In particular set [vpc settings](#set-vpc-settings)
4. Create infrastructure, see Operations [Apply](#terragrunt-apply)
6. Find dns name of aws load balancer in AWS console and open it in web browser

## Operations

### Set VPC settings
Use `./terraform/live/<new_env>/<region>/partition.hcl` file to set VPC settings: cidr, subnets etc

### Terragrunt plan

To check configuration across entire partition
```
cd terraform/live/dev/eu-central-1
terragrunt run-all plan
```
### Terragrunt apply

!!Do it carefully!! To apply configuration across entire partition.
```
cd .terraform/live/dev/eu-central-1
terragrunt run-all apply
```
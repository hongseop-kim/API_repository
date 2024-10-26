# API_repository

## project
#### [app]
##### 1. app_main.py                  # FastAPI API 서버 코드
##### 2. db_config.py              # DB 설정 파일


## [charts]


## [k8s]
##### 1.Deploy - Nginx,Tomcat.yaml       
##### 2.Namespace - Nginx, Tomcat.yaml
##### 3.Service - Nginx, Tomcat.yaml
##### 4.PV - Nginx, Tomcat.yaml
##### 5.PVC - Nginx, Tomcat
##### 6.Storage Class.yaml
##### 7.HPA - Nginx, Tomcat.yaml

## [terraform]
##### 1.acm.tf
##### 2.db.tf
##### 3.ec2.tf
##### 4.ecr.tf
##### 5.efs.tf
##### 6.eks.tf
##### 7.node.tf
##### 8.peering.tf
##### 9.provider.tf
##### 10.redis.tf
##### 11.route53.tf
##### 12.s3.tf
##### 13.sg.tf
##### 14.subnet.tf
##### 15.vpc.tf
##### 16.vpn.tf
---


# 프로젝트 개요

이 프로젝트는 AWS와 Kubernetes를 사용하여 FastAPI 애플리케이션과 MySQL 데이터베이스를 배포하는 예시입니다.

## 디렉터리 구조

- `app/`: 애플리케이션 코드
- `charts/`: Kubernetes Helm 차트
- `k8s/`: Kubernetes 리소스 매니페스트
- `terraform/`: 인프라 설정

## 배포 방법

1. `terraform` 디렉토리에서 Terraform을 사용하여 인프라를 배포합니다.
2. `charts` 디렉토리에서 Helm 차트를 사용하여 애플리케이션을 배포합니다.
3. 애플리케이션은 `app/main_app.py`에서 FastAPI 서버로 실행됩니다.

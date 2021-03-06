# 1.  Please prepare a release process from code commit to a production deployment to kubernetes cluster. It can be graphical or written.

import turtle

turtle.setup(1500, 350)
turtle.penup()
turtle.hideturtle()
turtle.goto(-200, 100)
turtle.write('From code commit to a production deployment to Kubernetes cluster')

turtle.speed(2)

Y = 0

DEVELOPERS_X = -700
COMMIT_X = -675
GIT_REPOSITORY_X = -575
TRIGGER_BUILD_X = -400
JENKINS_X = -320
CREATE_PUSH_DOCKER_IMAGE_X = -100
DOCKER_REGISTRY_X = 50
DEPLOYMENT_X = 250
DOCKER_ORCHESTRATION_X = 370

COMMENT_Y = -50

END_USERS_X = 600
END_USERS_Y = -50


turtle.goto(DEVELOPERS_X, Y+50)
turtle.write('DEVELOPERS')
turtle.goto(DEVELOPERS_X, Y+25)
turtle.write('Continuous Integration')
turtle.goto(END_USERS_X, END_USERS_Y)
turtle.write('END USERS')
turtle.goto(END_USERS_X, END_USERS_Y-20)
turtle.write('Monitor')

turtle.goto(COMMIT_X, Y)
turtle.write('CODE | Commit')
turtle.pendown()
turtle.goto(GIT_REPOSITORY_X, Y)
turtle.dot()
turtle.write('GIT REPOSITORY')
turtle.pendown()
turtle.goto(TRIGGER_BUILD_X, Y)
turtle.write('Trigger Build')
turtle.pendown()
turtle.goto(JENKINS_X, Y)
turtle.dot()
turtle.write('BUILD, TEST, DEPLOY')
turtle.pendown()
turtle.goto(CREATE_PUSH_DOCKER_IMAGE_X, Y)
turtle.write('Create & Push Docker Image')
turtle.pendown()
turtle.goto(DOCKER_REGISTRY_X, Y)
turtle.dot()
turtle.write('DOCKER REGISTRY')
turtle.pendown()
turtle.goto(DEPLOYMENT_X, Y)
turtle.write('Deployment')
turtle.pendown()
turtle.goto(DOCKER_ORCHESTRATION_X, Y)
turtle.dot()
turtle.write('DOCKER ORCHESTRATION')
turtle.penup()


turtle.goto(GIT_REPOSITORY_X, COMMENT_Y)
turtle.dot()
turtle.write('GitHub')
turtle.goto(JENKINS_X, COMMENT_Y)
turtle.dot()
turtle.write('Jenkins')
turtle.goto(JENKINS_X, COMMENT_Y-30)
turtle.write('Pipeline')
turtle.goto(DOCKER_REGISTRY_X, COMMENT_Y)
turtle.dot()
turtle.write('Artifactory')
turtle.goto(DOCKER_ORCHESTRATION_X, COMMENT_Y)
turtle.dot()
turtle.write('K8S')
turtle.goto(DOCKER_ORCHESTRATION_X, COMMENT_Y-30)
turtle.write('Pods in Nodes')

turtle.goto(TRIGGER_BUILD_X-50, Y)
turtle.dot()
turtle.pendown()
turtle.goto(TRIGGER_BUILD_X-50, Y-100)
turtle.penup()
turtle.goto(TRIGGER_BUILD_X-50, Y-120)
turtle.write('Docker-compose')
turtle.goto(TRIGGER_BUILD_X-50, Y-135)
turtle.write('.yml')
turtle.penup()

turtle.goto(DEPLOYMENT_X, Y)
turtle.dot()
turtle.pendown()
turtle.goto(DEPLOYMENT_X, Y-100)
turtle.penup()
turtle.goto(DEPLOYMENT_X, Y-120)
turtle.write('Infrastructure as a Code')
turtle.goto(DEPLOYMENT_X, Y-135)
turtle.write('Cloud-EC2 | Terraform (optional)')
turtle.penup()

turtle.goto(-100, -150)
turtle.write('Continuous Deployment')

turtle.done()

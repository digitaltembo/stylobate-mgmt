def container_name(is_dev):
    return ('dev' if is_dev else 'prod') + '-stylobate'

def image_name(username_args, is_dev):
    docker_prefix = username_args[0] + '/' if username_args else ''
    return docker_prefix + container_name(is_dev)

def build_command(username_args, is_dev):
    return 'docker build -f docker/Dockerfile.{} -t {} .'.format('dev' if is_dev else 'prod', image_name(username_args, is_dev))

def run_command(username_args, is_dev):
    if is_dev:
        return '''
            docker run
                    -it
                    -d
                    --name {}
                    -p 3000:3000
                    -p 8000:8000
                    -e PORT="8000"
                    -v $(pwd)/backend:/app
                    -v $(pwd)/frontend:/frontend
                    {} /docker-dev-start.sh
        '''.format(container_name(is_dev), image_name(username_args, is_dev))
    else:
        return '''
            docker run
                -it
                -d
                --name {}
                -p 80:80
                -e PORT="80"
                -e IS_PROD="TRUE"
                -e SECRET_KEY=$(uuidgen)
            {} /docker-prod-start.sh"
        '''.format(container_name(is_dev), image_name(username_args, is_dev))


def logs_command(container_name, style):
    if style == 'less':
        return 'docker logs {} | less'.format(container_name)
    elif style == 'cat':
        return 'docker logs {}'.format(container_name)
    else:
        return 'docker logs -f {}'.format(container_name)


def shell_command(container_name):
    return 'docker exec -it {} /bin/bash'.format(container_name)

def stop_command(container_name):
    return 'docker container stop {} && docker rm {}'.format(container_name, container_name)



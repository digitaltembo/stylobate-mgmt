# docker configurations
DEV = 'dev-compose.yaml'
PROD = 'prod-compose.yaml'
SSL = 'ssl-compose.yaml'

# docker images
CERTBOT = 'certbot'
NGINX = 'nginx'
BACKEND = 'backend'
FRONTEND = 'frontend'

AVAILABLE_DOCKER_CONTAINERS = {
    DEV: [BACKEND, FRONTEND],
    PROD: [BACKEND, NGINX],
    SSL: [BACKEND, NGINX, CERTBOT]
}


def get_env(args):
    if args.docker_prod:
        return  PROD
    if args.docker_ssl:
        return  SSL
    return DEV

def get_img(args):
    if args.certbot:
        return CERTBOT
    if args.nginx:
        return NGINX
    if args.front_end:
        return FRONTEND
    return BACKEND

def env_has_container(docker_env, docker_container):
    return docker_container in AVAILABLE_DOCKER_CONTAINERS[docker_env]

def container_name(project_name, docker_env, docker_container):

    suffix = ''
    if docker_env == PROD:
        suffix = '_prod'
    elif docker_env == SSL:
        suffix = '_ssl'
    return '{}_{}{}_1'.format(project_name, docker_container, suffix)

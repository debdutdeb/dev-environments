from docker import DockerClient, from_env as get_docker_client

from store import Store

import os
'''
1. start the container
2. create user with correct uid
3. setup neovim correctly
4. attach the container to stdin stdout and stderr
5. on exit take a snapshot
'''


class UidGidRequiredException(Exception):
    fmt: str = (
        'Both UID and GID environment variables are required for safe environment setup'
        'Without them you may face permission issues long term'
        'Please set them manually if not set in environment for some reason'
        'Or use the --uid/--gid options')

    def __repr__(self) -> str:
        return self.fmt


class Environment:

    def __init__(self: 'Environment',
                 project: str,
                 store: Store,
                 uid: str = None,
                 gid: str = None):
        self.client = get_docker_client()

        self.project = project

        self.store = store

        self.uid = os.getenv('UID', uid)
        self.gid = os.getenv('GID', gid)
        if self.uid is None or self.gid is None:
            raise UidGidRequiredException
    @property
    def base_container_config(self):
        return {'image': "debdutdeb/dev-environment-linux:dind-rootless",
            auto_remove=False,
            name=self.project,
            network_mode='host',
            oom_kill_disable=False,
            privileged=True,
            restart_policy={
                'Name': 'on-failure',
                'MaximumRetryCount': 5
            },
            version='auto',
            volumes={})

    def find_project_environment_snapshot(self) -> str:
        '''Returns container snapped image for a project'''

    def _start_container(self):
        self.client.containers.create(
            image="debdutdeb/dev-environment-linux:dind-rootless",
            auto_remove=False,
            name=self.project,
            network_mode='host',
            oom_kill_disable=False,
            privileged=True,
            restart_policy={
                'Name': 'on-failure',
                'MaximumRetryCount': 5
            },
            version='auto',
            volumes={})

    def _init_neovim(self) -> None:
        pass

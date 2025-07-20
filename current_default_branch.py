from git import Repo


def current_default_branch():
    repo = Repo(search_parent_directories=True)
    return repo.remotes.origin.refs["HEAD"].reference.remote_head

if __name__ == "__main__":
    print(current_default_branch())
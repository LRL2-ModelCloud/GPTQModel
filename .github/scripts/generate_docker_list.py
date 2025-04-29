import json


def get_version_list():
    cu_list = [118, 121, 124, 126, 128]
    cp_list = [39, 310, 311, 312, 313] #
    torch_list = ["2.0.1", "2.1.2", "2.2.2", "2.3.1", "2.4.1", "2.5.1", "2.6.0", "2.7.0"] #

    results = []

    for torch in torch_list:
        for cu in cu_list:
            for cp in cp_list:
                if ((torch == "2.0.1" and cu == 118 and cp < 312) or
                        (torch == "2.1.2" and cu < 124 and cp < 312) or
                        (torch == "2.2.2" and cu < 124 and cp < 313) or
                        (torch == "2.3.1" and cu < 124 and cp < 313) or
                        (torch == "2.4.1" and cu < 126 and cp < 313) or
                        (torch == "2.5.1" and cu < 126) or
                        (torch == "2.6.0" and cu >= 126) or
                        (torch == "2.7.0" and cu >= 126)
                ):
                    version_name = f"compiler_cuda{cu}-torch{torch}-python{cp}"
                    results.append(version_name)
    return results

if __name__ == '__main__':
    print(json.dumps(get_version_list()))
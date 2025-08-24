from typing import Any, List, Tuple

def flatten_list(data: Any) -> List[Any]:
    """
    İç içe listeleri/tuple'ları düzleştirir.
    String/bytes gibi dizileri bozmaz.
    """
    out: List[Any] = []

    def _walk(x: Any):
        if isinstance(x, (list, tuple)):
            for item in x:
                _walk(item)
        else:
            out.append(x)

    _walk(data)
    return out


def deep_reverse(data: Any) -> Any:
    """
    Listeyi ve tüm alt listeleri tersine çevirir.
    Liste değilse olduğu gibi döner.
    """
    if isinstance(data, list):
        return [deep_reverse(x) for x in reversed(data)]
    return data


if __name__ == "__main__":
    # Demo
    inp1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
    print(flatten_list(inp1))  # [1,'a','cat',2,3,'dog',4,5]

    inp2 = [[1, 2], [3, 4], [5, 6, 7]]
    print(deep_reverse(inp2))  # [[7,6,5], [4,3], [2,1]]

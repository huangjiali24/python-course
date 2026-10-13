def parse_student(line):
    parts = line.strip().split(",")
    if len(parts) != 2:
        raise ValueError("字段数量不正确")
    name, score_str = parts
    if not name:
        raise ValueError("姓名不能为空")
    score = int(score_str)
    if score < 0 or score > 100:
        raise ValueError("成绩必须在 0 到 100 之间")
    return {"name": name, "score": score}

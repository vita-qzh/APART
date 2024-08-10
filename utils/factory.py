def get_model(model_name, args):
    name = model_name.lower()
    if name == "apart":
        from models.apart import Learner
    else:
        assert 0
    
    return Learner(args)

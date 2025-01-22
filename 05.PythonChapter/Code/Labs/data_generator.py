import numpy as np

def data_gen(data, bsize):
    """
    Generator function that yields mini-batches of data for training.
    
    Args:
        data (dict): Dictionary containing 'Input' and 'Target' arrays
        bsize (int): Mini-batch size - number of columns to yield at each iteration
        
    Yields:
        tuple: (epoch number, input mini-batch, target mini-batch)
    """
    In = data['Input']
    Tar = data['Target']
    num_samples = In.shape[1]  # Number of columns
    steps = num_samples // bsize  # Number of mini-batches per epoch
    epoch = 0
    
    while True:
        # Iterate through mini-batches
        for ii in range(steps):
            start_idx = ii * bsize
            end_idx = (ii + 1) * bsize
            yield epoch, In[:, start_idx:end_idx], Tar[:, start_idx:end_idx]
        
        # Shuffle the data after completing an epoch
        perm = np.random.permutation(num_samples)
        In = In[:, perm]  # Reorder columns using permutation
        Tar = Tar[:, perm]  # Use same permutation for targets
        epoch += 1

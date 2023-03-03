import DashboardIcon from '@mui/icons-material/Dashboard';
import SupervisedUserCircleIcon from '@mui/icons-material/SupervisedUserCircle';
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart';
import DesignServicesIcon from '@mui/icons-material/DesignServices';
import CampaignIcon from '@mui/icons-material/Campaign';
import StoreIcon from '@mui/icons-material/Store';
import ConstructionIcon from '@mui/icons-material/Construction';
import AssignmentIndIcon from '@mui/icons-material/AssignmentInd';


const navItems = [

    {
        label: 'Dashboard',
        to: '/dashboard',
        icon: <DashboardIcon />
    }, {
        label: 'Marketing',
        to: '/marketing',
        icon: <CampaignIcon />
    }, {
        label: 'Design',
        to: '/design',
        icon: <DesignServicesIcon />
    },
    {
        label: 'Purchase',
        to: '/purchase',
        icon: <ShoppingCartIcon />
    },
    {
        label: 'Store',
        to: '/store',
        icon: <StoreIcon />
    },
    {
        label: 'Production',
        to: '/production',
        icon: <ConstructionIcon />
    },
    {
        label: 'Accounts',
        to: '/accounts',
        icon: <AssignmentIndIcon />
    },
];


export default navItems;